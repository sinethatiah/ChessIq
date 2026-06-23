from datetime import datetime

class ChessGame():
    def __init__(self , raw , username):
        self.username=username.lower()

        self.colour= "white" if raw["white"]["username"].lower()==self.username else "black"
        my_side=raw[self.colour]
        opp_side=raw["black"] if self.colour== "white" else raw["white"]

        self.my_rating=my_side["rating"]
        self.opp_rating=opp_side["rating"]
        self.result=my_side["result"]

        eco_url=raw.get("eco", "")
        self.opening=eco_url.split("/")[-1] if eco_url else "unknown"

        self.time_class=raw["time_class"]
        self.date=datetime.utcfromtimestamp(raw["end_time"])

        self.pgn=raw["pgn"]
        

    def is_win(self):
            return self.result == "win"

    def is_loss(self):
            return self.result not in ["win", "agreed", "repetition", "stalemate", "insufficient", "50move"]
    def was_time_loss(self):
            return self.result == "timeout"
    def rating_delta(self, prev_rating):
            return self.my_rating - prev_rating
    def outcome(self):
            if self.result == "win":
                return "win"
            elif self.result in ["agreed", "repetition", "stalemate", "insufficient", "50move"]:
                return "draw"
            else:
                return "loss"
    def to_dict(self):
            return {
                "date": self.date.isoformat(),
                "color": self.colour,
                "my_rating": self.my_rating,
                "opp_rating": self.opp_rating,
                "result": self.result,
                "outcome": self.outcome(),
                "opening": self.opening,
                "time_class": self.time_class,
                "was_time_loss": self.was_time_loss(),
            }
        