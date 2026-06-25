import tkinter as tk
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

USERNAME = "grandlord500"
TIME_CONTROLS = ["rapid", "blitz"]

def load_games():
    raw_games=fetch_all_games(USERNAME)
    return[ChessGame(g, USERNAME) for g in raw_games if g["time_class"] in TIME_CONTROLS]

def onclick():
    btn.config(text="loading..." , state="disabled")
    root.update()
    games=load_games()
    build_tabs(games)
    btn.config(text="Done!", state="disabled")

def build_tabs(games):
    for tab in notebook.tabs():
        notebook.forget(tab)

    #colour tab
    frame = tk.Frame(notebook)
    notebook.add(frame, text="Colour")
    results = win_rate_by_colour(games)
    headers = ("Colour", "Win%", "Draw%", "Loss%", "Games")
    rows = [(c.capitalize(), d["win%"], d["draw%"], d["loss%"], d["total"])
            for c, d in results.items()]
    make_table(frame, headers, rows)

    # Openings tab
    frame = tk.Frame(notebook)
    notebook.add(frame, text="Openings")
    openings = win_rate_by_opening(games)
    sorted_openings = sorted(openings.items(), key=lambda x: x[1]["total"], reverse=True)
    headers = ("Opening", "Win%", "Draw%", "Loss%", "Games")
    rows = [(o.replace("-", " ")[:50], d["win%"], d["draw%"], d["loss%"], d["total"])
            for o, d in sorted_openings[:20]]
    make_table(frame, headers, rows)

    # Hours tab
    frame = tk.Frame(notebook)
    notebook.add(frame, text="Hours (UTC)")
    hourly = performance_by_hour(games)
    sorted_hours = sorted(hourly.items())
    headers = ("Hour", "Win%", "Draw%", "Loss%", "Games")
    rows = [(f"{str(h).zfill(2)}:00", d["win%"], d["draw%"], d["loss%"], d["total"])
            for h, d in sorted_hours]
    make_table(frame, headers, rows)



def make_table(frame, headers, rows):
    tree = ttk.Treeview(frame, columns=headers, show="headings")
    for col in headers:
        tree.heading(col, text=col)
        tree.column(col, width=160, anchor="center")
    for row in rows:
        tree.insert("", "end", values=row)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

root=tk.Tk()
root.title("chessIQ")
root.geometry("900x600")

title_label = tk.Label(root, text="ChessIQ", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

subtitle_label = tk.Label(root, text=f"Analytics for {USERNAME}", font=("Arial", 12))
subtitle_label.pack()

btn = tk.Button(root, text="Generate Report", font=("Arial", 12), command=onclick)
btn.pack(pady=15)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)


root.mainloop()
