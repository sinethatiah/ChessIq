import requests

BASE_URL = "https://api.chess.com/pub/player"

HEADERS = {
    "User-Agent": "ChessIQ/1.0"
}

def fetch_archives(username):
    url=f"{BASE_URL}/{username}/games/archives"
    response= requests.get(url , headers=HEADERS)
    data=response.json()
    return data["archives"]

def fetch_games(url):
    response= requests.get(url , headers=HEADERS)
    data=response.json()
    return data["games"]

