import sqlite3

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