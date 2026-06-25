import tkinter as tk
from tkinter import ttk

from chess_tracker.api_client import fetch_all_games
from chess_tracker.models import ChessGame

USERNAME = "grandlord500"
TIME_CONTROLS = ["rapid", "blitz"]

def load_games():
    raw_games=fetch_all_games(USERNAME)
    return[ChessGame(g, USERNAME) for g in raw_games if g["time_class"] in TIME_CONTROLS]

def onclick():
    btn.config(text="loading..." , state="disabled")
    root.update()
    games=load_games()
    btn.config(text="Done!", state="disabled")

root=tk.Tk()
root.title("chessIQ")
root.geometry("900x600")

title_label = tk.Label(root, text="ChessIQ", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

subtitle_label = tk.Label(root, text=f"Analytics for {USERNAME}", font=("Arial", 12))
subtitle_label.pack()

btn = tk.Button(root, text="Generate Report", font=("Arial", 12), command=onclick)
btn.pack(pady=15)

root.mainloop()
