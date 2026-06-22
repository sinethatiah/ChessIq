from chess_tracker.api_client import fetch_all_games

all_games = fetch_all_games("grandlord500")
# print(f"Total games fetched: {len(all_games)}")
import json
print(json.dumps(all_games[0], indent=2))

