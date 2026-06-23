from chess_tracker.api_client import fetch_all_games
from chess_tracker.models import ChessGame
import json
from chess_tracker.analysis import win_rate_by_colour

all_games = fetch_all_games("grandlord500")
# print(f"Total games fetched: {len(all_games)}")

# print(json.dumps(all_games[0], indent=2))

raw_games=fetch_all_games("grandlord500")
games = [ChessGame (g, "grandlord500") for g in raw_games if g["time_class"]== "rapid"]
# print(f"Rapid games: {len(games)}")
# print(games[0].to_dict())
results=win_rate_by_colour(games)
for colour, data in results.items():
    print(f"{colour}:{data}")