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