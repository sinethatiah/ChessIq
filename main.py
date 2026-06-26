from chess_tracker.api_client import fetch_all_games
from chess_tracker.models import ChessGame
import json
from chess_tracker.analysis import win_rate_by_colour , win_rate_by_opening, performance_by_hour, rating_over_time, win_rate_by_opponent_gap , streak_tracking , time_trouble_rate

# all_games = fetch_all_games("grandlord500")
# print(f"Total games fetched: {len(all_games)}")

# print(json.dumps(all_games[0], indent=2))

raw_games=fetch_all_games("grandlord500")
games = [ChessGame (g, "grandlord500") for g in raw_games if g["time_class"]== "rapid"]
# print(f"Rapid games: {len(games)}")
# print(games[0].to_dict())

"""
analysis by colour
"""
# results=win_rate_by_colour(games)
# for colour, data in results.items():
#     print(f"{colour}:{data}")


# openings = win_rate_by_opening(games)
# for opening, data in openings.items():
#     print(f"{opening}: {data}")

"""
analysis by opening 
"""
# openings = win_rate_by_opening(games)
# print(f"Total games: {len(games)}")
# print(f"Total openings found: {len(openings)}")
# print(games[0].opening)
# print(games[1].opening)
# print(games[2].opening)
# sorted_openings = sorted(openings.items(), key=lambda x: x[1]["total"], reverse=True)
# for opening, data in sorted_openings[:15]:
#     print(f"{opening}: {data}")

"""
analysis by hours
"""
# hourly = performance_by_hour(games)
# sorted_hours = sorted(hourly.items())
# for hour, data in sorted_hours:
#     print(f"{hour:02d}:00 - {data}")

"""
tracking rating with time
"""
# ratings=rating_over_time(games)
# for entry in ratings[:10]:
#     print(entry)

"""
analysis of opponent rating gap
"""
# gaps = win_rate_by_opponent_gap(games)
# for bucket, data in gaps.items():
#     print(f"{bucket}: {data}")

"""
tracking of streaks
"""
# streaks=streak_tracking(games)
# print(streaks)

"""
analysis of loss rate due to time
"""
# time_trouble = time_trouble_rate(games)
# for month, data in time_trouble.items():
#     print(f"{month}: {data}")


