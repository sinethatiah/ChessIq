# ChessIQ
 
*A personal chess analytics tool built on chess.com game history*
 
## Problem Statement
 
Chess.com's own stats page is shallow — it shows win/loss totals and a rating graph, and not much else. If you actually want to know whether your opening choices are working, whether you're losing games to the clock more than to bad moves, or whether your rating climbs are predictable or random, you're left scrolling through hundreds of individual games by hand. There's no way to see the patterns across your full history in one place.
 
## Solution
 
ChessIQ pulls your entire game history straight from the chess.com public API, models each game as a structured object, and stores it in a local database. From there it runs a set of analyses — rating trends, opening performance, time-management patterns, and (optionally) blunder frequency via Stockfish — turning roughly 450 games of raw data into a personal diagnostic report you can actually act on.
 
## Features
 
- **Automated data pull** — fetches your entire game history from chess.com, no manual exporting
- **Rating trajectory tracking** — visualize rating over time, identify plateaus and breakthroughs
- **Opening win-rate breakdown** — win/loss/draw percentage grouped by opening family
- **Color performance split** — White vs Black win rates
- **Opponent-strength performance** — win rate bucketed by rating gap vs opponent
- **Time-trouble detection** — percentage of losses caused by running out of clock, tracked over time
- **Time-of-day performance** — checks whether play quality shifts by hour or day of week
- **Streak tracking** — longest win/loss runs in your history
- **Blunder detection (stretch goal)** — Stockfish-powered analysis flagging significant evaluation drops, move by move
## Technology Used
 
- **Python 3** — core language
- **requests** — chess.com API calls
- **python-chess** — PGN parsing, opening identification, Stockfish (UCI) interface
- **SQLite** — local data storage
- **Stockfish** — free, open-source chess engine (used for blunder detection)
- **matplotlib** — optional, for charting rating trends and win rates
## Project Structure
 
```
chess-analytics/
├── data/
│   └── games.db                 # SQLite database
├── chess_tracker/
│   ├── __init__.py
│   ├── api_client.py            # chess.com API calls
│   ├── models.py                # ChessGame class
│   ├── database.py              # SQLite read/write
│   ├── analysis.py              # stats functions
│   └── engine.py                # Stockfish blunder detection (stretch goal)
├── main.py                      # entry point, ties everything together
├── requirements.txt
└── README.md
```
 
## Environment Setup
 
To run this project locally you will need Python 3 installed. Stockfish is only required if you want the blunder-detection feature.
 
### Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
 
### Install Dependencies
```powershell
pip install -r requirements.txt
```
or, if requirements.txt isn't generated yet:
```powershell
pip install requests python-chess
```
 
### Chess.com API
No API key or signup required — the public endpoints are open to anyone.
 
 
## Running Locally
 
```powershell
python main.py --update     # pulls any new games and stores them
python main.py --report     # prints/generates your stats report
```
 
## Contributing
 
Contributions are welcome. If you find a bug or have a feature idea, open an issue on GitHub before starting work so it can be discussed first.
 
1. Fork the repository
2. Clone your fork locally:
```
   git clone https://github.com/yourusername/ChessIQ.git
```
3. Install dependencies:
```
   pip install -r requirements.txt
```
4. Create a new branch for your feature:
```
   git checkout -b feature/your-feature
```
5. Make your changes and commit:
```
   git commit -m "Add your feature"
```
6. Push to your branch:
```
   git push origin feature/your-feature
```
7. Open a pull request on the original repository
## Licensing
 
This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.