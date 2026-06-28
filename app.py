# import tkinter as tk
# from tkinter import ttk

import customtkinter as ctk
from tkinter import ttk



from chess_tracker.api_client import fetch_all_games
from chess_tracker.models import ChessGame
from chess_tracker.analysis import (
    win_rate_by_colour,
    win_rate_by_opening,
    performance_by_hour,
    rating_over_time,
    win_rate_by_opponent_gap,
    streak_tracking,
    time_trouble_rate
)

from chess_tracker.database import init_db, insert_many, get_all_games, is_empty, DBGame

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


USERNAME = "grandlord500"
TIME_CONTROLS = ["rapid", "blitz"]

def load_games():
    init_db()
    if is_empty():
        print("Fetching from API...")
        raw_games = fetch_all_games(USERNAME)
        games = [ChessGame(g, USERNAME) for g in raw_games if g["time_class"] in TIME_CONTROLS]
        insert_many(games)
    rows = get_all_games()
    return [DBGame(row) for row in rows]

def onclick():
    btn.configure(text="Loading...", state="disabled")
    root.update()
    games = load_games()
    build_tabs(games, notebook)
    btn.configure(text="Done!", state="disabled")

def build_tabs(games , notebook):
    for tab in notebook.tabs():
        notebook.forget(tab)

    #colour tab
    frame = ctk.CTkFrame(notebook)
    notebook.add(frame, text="Colour")
    results = win_rate_by_colour(games)
    headers = ("Colour", "Win%", "Draw%", "Loss%", "Games")
    rows = [(c.capitalize(), d["win%"], d["draw%"], d["loss%"], d["total"])
            for c, d in results.items()]
    make_table(frame, headers, rows)

    # Openings tab
    frame = ctk.CTkFrame(notebook)
    notebook.add(frame, text="Openings")
    openings = win_rate_by_opening(games)
    sorted_openings = sorted(openings.items(), key=lambda x: x[1]["total"], reverse=True)
    headers = ("Opening", "Win%", "Draw%", "Loss%", "Games")
    rows = [(o.replace("-", " ")[:50], d["win%"], d["draw%"], d["loss%"], d["total"])
            for o, d in sorted_openings[:20]]
    make_table(frame, headers, rows)

    # Hours tab
    frame = ctk.CTkFrame(notebook)
    notebook.add(frame, text="Hours (UTC)")
    hourly = performance_by_hour(games)
    sorted_hours = sorted(hourly.items())
    headers = ("Hour", "Win%", "Draw%", "Loss%", "Games")
    rows = [(f"{str(h).zfill(2)}:00", d["win%"], d["draw%"], d["loss%"], d["total"])
            for h, d in sorted_hours]
    make_table(frame, headers, rows)

    # Opponent strength tab
    frame = ctk.CTkFrame(notebook)
    notebook.add(frame, text="Opponent Strength")
    gaps = win_rate_by_opponent_gap(games)
    headers = ("Bucket", "Win%", "Draw%", "Loss%", "Games")
    rows = [(b, d["win%"], d["draw%"], d["loss%"], d["total"])
            for b, d in gaps.items() if d["total"] > 0]
    make_table(frame, headers, rows)

     # Streaks tab
    frame = ctk.CTkFrame(notebook)
    notebook.add(frame, text="Streaks")
    streaks = streak_tracking(games)
    headers = ("Metric", "Value")
    rows = [
        ("Best win streak", streaks["best_win_streak"]),
        ("Best loss streak", streaks["best_loss_streak"]),
        ("Current win streak", streaks["current_win_streak"]),
        ("Current loss streak", streaks["current_loss_streak"]),
    ]
    make_table(frame, headers, rows)

    # Time trouble tab
    frame = ctk.CTkFrame(notebook)
    notebook.add(frame, text="Time Trouble")
    tt = time_trouble_rate(games)
    headers = ("Month", "Time Losses", "Total Losses", "Games", "% of Losses")
    rows = [(m, d["time_losses"], d["total_losses"], d["total_games"], f"{d['time_loss%']}%")
            for m, d in tt.items()]
    make_table(frame, headers, rows)

    # Rating tab
    frame = ctk.CTkFrame(notebook)
    notebook.add(frame, text="Rating")
    ratings = rating_over_time(games)
    headers = ("Date", "Rating", "Time Class")
    rows = [(r["date"][:10], r["rating"], r["time_class"]) for r in ratings]
    make_table(frame, headers, rows)


def make_table(frame, headers, rows):
    style = ttk.Style()
    style.configure("Treeview", font=("Arial", 12), rowheight=30)
    style.configure("Treeview.Heading", font=("Arial", 13, "bold"))
    
    tree = ttk.Treeview(frame, columns=headers, show="headings")
    for col in headers:
        tree.heading(col, text=col)
        tree.column(col, width=200, anchor="center")
    for row in rows:
        tree.insert("", "end", values=row)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

root = ctk.CTk()
root.title("chessIQ")
root.geometry("1100x700")

style = ttk.Style()
style.theme_use("clam")
style.configure("TNotebook", background="#2b2b2b", borderwidth=0)
style.configure("TNotebook.Tab", background="#2b2b2b", foreground="white", padding=[10, 5])
style.configure("Treeview", background="#2b2b2b", foreground="white", fieldbackground="#2b2b2b", rowheight=25)
style.configure("Treeview.Heading", background="#1f1f1f", foreground="white")
style.map("TNotebook.Tab", background=[("selected", "#1f6aa5")])

title_label = ctk.CTkLabel(root, text="ChessIQ", font=("Arial", 32, "bold"))
title_label.pack(pady=20)

subtitle_label = ctk.CTkLabel(root, text=f"Analytics for {USERNAME}", font=("Arial", 14))
subtitle_label.pack()

btn = ctk.CTkButton(root, text="Generate Report", font=("Arial", 12), command=onclick)
btn.pack(pady=15)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)


root.mainloop()
