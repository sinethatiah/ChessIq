import sqlite3
from datetime import datetime

DB_PATH = "data/games.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            colour TEXT,
            my_rating INTEGER,
            opp_rating INTEGER,
            result TEXT,
            outcome TEXT,
            opening TEXT,
            time_class TEXT,
            was_time_loss INTEGER
        )
    """)
    conn.commit()
    conn.close()

def insert_game(game):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO games (date, colour, my_rating, opp_rating, result, outcome, opening, time_class, was_time_loss)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        game.date.isoformat(),
        game.colour,
        game.my_rating,
        game.opp_rating,
        game.result,
        game.outcome(),
        game.opening,
        game.time_class,
        int(game.was_time_loss())
    ))
    conn.commit()
    conn.close()

def insert_many(games):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executemany("""
        INSERT INTO games (date, colour, my_rating, opp_rating, result, outcome, opening, time_class, was_time_loss)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [
        (
            g.date.isoformat(),
            g.colour,
            g.my_rating,
            g.opp_rating,
            g.result,
            g.outcome(),
            g.opening,
            g.time_class,
            int(g.was_time_loss())
        )
        for g in games
    ])
    conn.commit()
    conn.close()

def get_all_games():
    conn =sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games")
    rows= cursor.fetchall()
    conn.close()
    return rows


def is_empty():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM games")
    count= cursor.fetchone()[0]
    conn.close()
    return count == 0


def row_to_dict(row):
    keys = ["id", "date", "colour", "my_rating", "opp_rating",
            "result", "outcome", "opening", "time_class", "was_time_loss"]
    return dict(zip(keys, row))

class DBGame:
    def __init__(self, row):
        d = row_to_dict(row)
        self.date = datetime.fromisoformat(d["date"])
        self.colour = d["colour"]
        self.my_rating = d["my_rating"]
        self.opp_rating = d["opp_rating"]
        self.result = d["result"]
        self._outcome = d["outcome"]
        self.opening = d["opening"]
        self.time_class = d["time_class"]
        self._was_time_loss = bool(d["was_time_loss"])

    def outcome(self):
        return self._outcome

    def was_time_loss(self):
        return self._was_time_loss

    def is_win(self):
        return self._outcome == "win"

    def is_loss(self):
        return self._outcome == "loss"