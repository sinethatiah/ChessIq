import tkinter as tk

root=tk.Tk()
root.title("chessIQ")
root.geometry("900x600")

title_label = tk.Label(root, text="ChessIQ", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

root.mainloop()
