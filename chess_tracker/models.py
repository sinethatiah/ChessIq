from datetime import datetime

class chessGame():
    def __init__(self , raw , username):
        self.username=username.lower()

        self.colour= "white" if raw["white"]["username"].lower()==self.username else "black"
        my_side=raw[self.colour]
        opp_side=raw["black"] if self.colour== "white" else raw["black"]

        self.my_rating=my_side["rating"]
        self.opp_rating=opp_side["rating"]

        eco_url=raw.get("eco", "")
        self.opening=eco_url.split("/")[-1] if eco_url else "unknown"

        self.time_class=raw["time_class"]
        self.date=datetime.utcfromtimestamp(raw["end_time"])

        self.pgn=raw["pgn"]
    