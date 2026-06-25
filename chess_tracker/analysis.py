def win_rate_by_colour(games):
    results={
        "white":{"win":0,"draw":0, "loss":0, "total":0 },
        "black":{"win":0,"draw":0, "loss":0, "total":0 }
    }
    for game in games:
        colour=game.colour
        outcome=game.outcome()
        results[colour][outcome]+=1
        results[colour]["total"]+=1
    for colour , data in results.items():
        total=data["total"]
        if total > 0:
            data["win%"] = round(data["win"] / total * 100, 1)
            data["draw%"] = round(data["draw"] / total * 100, 1)
            data["loss%"] = round(data["loss"] / total * 100, 1)
    return results


def win_rate_by_opening(games):
    results={}
    for game in games:
        opening=game.opening
        outcome=game.outcome()
        if opening not in results:
            results[opening]={"win": 0, "draw": 0, "loss": 0, "total": 0}
        results[opening][outcome]+=1
        results[opening]["total"]+=1
    
    for opening, data in results.items():
        total=data["total"]
        if total > 0:
            data["win%"] = round(data["win"] / total * 100, 1)
            data["draw%"] = round(data["draw"] / total * 100, 1)
            data["loss%"] = round(data["loss"] / total * 100, 1)
    return results

def performance_by_hour(games):
    results={}
    for game in games:
        hour=game.date.hour
        outcome=game.outcome()
        if hour not in results:
            results[hour]={"win": 0, "draw": 0, "loss": 0, "total": 0}
        results[hour][outcome]+=1
        results[hour]["total"]+=1

    for hour, data in results.items():
        total=data["total"]
        if total > 0:
            data["win%"] = round(data["win"] / total * 100, 1)
            data["draw%"] = round(data["draw"] / total * 100, 1)
            data["loss%"] = round(data["loss"] / total * 100, 1)
    return results

def rating_over_time(games):
    sorted_games=sorted(games, key=lambda x: x.date)
    results=[]

    for game in sorted_games:
        results.append({
            "date":game.date.isoformat(),
            "rating":game.my_rating,
            "time_class":game.time_class
        })
    return results

def win_rate_by_opponent_gap(games):
    results = {
        "much stronger (>100)": {"win": 0, "draw": 0, "loss": 0, "total": 0},
        "stronger (50-100)": {"win": 0, "draw": 0, "loss": 0, "total": 0},
        "even (-50 to 50)": {"win": 0, "draw": 0, "loss": 0, "total": 0},
        "weaker (50-100)": {"win": 0, "draw": 0, "loss": 0, "total": 0},
        "much weaker (>100)": {"win": 0, "draw": 0, "loss": 0, "total": 0},
    }
    for game in games:
        gap=game.opp_rating - game.my_rating
        outcome=game.outcome()
        if gap > 100:
            bucket = "much stronger (>100)"
        elif gap > 50:
            bucket = "stronger (50-100)"
        elif gap >= -50:
            bucket = "even (-50 to 50)"
        elif gap >= -100:
            bucket = "weaker (50-100)"
        else:
            bucket = "much weaker (>100)"

        results[bucket][outcome] += 1
        results[bucket]["total"] += 1
    for bucket , data in results.items():
        total = data["total"]
        if total > 0:
            data["win%"] = round(data["win"] / total * 100, 1)
            data["draw%"] = round(data["draw"] / total * 100, 1)
            data["loss%"] = round(data["loss"] / total * 100, 1)

    return results

def streak_tracking(games):
    sorted_games = sorted(games, key=lambda x: x.date)

    current_streak = {"type": None, "count": 0}
    best_win_streak = 0
    best_loss_streak = 0
    current_win_streak = 0
    current_loss_streak = 0

    for game in sorted_games:
        outcome=game.outcome()
        if outcome == "win":
            current_win_streak+=1
            current_loss_streak=0
            if current_win_streak>best_win_streak:
                best_win_streak=current_win_streak
        elif outcome=="loss":
            current_loss_streak+=1
            current_win_streak=0
            if current_loss_streak>best_loss_streak:
                best_loss_streak=current_loss_streak
        else:
            current_win_streak=0
            current_loss_streak=0
    return {
        "best_win_streak": best_win_streak,
        "best_loss_streak": best_loss_streak,
        "current_win_streak": current_win_streak,
        "current_loss_streak": current_loss_streak,
    }

def time_trouble_rate(games):
    sorted_games = sorted(games, key=lambda x: x.date)

    monthly={}
    
    for game in sorted_games:
        month= game.date.strftime("%Y-%m")
        outcome=game.outcome()

        if month not in monthly:
            monthly[month] = {"time_losses": 0, "total_losses": 0, "total_games": 0}
    
        monthly[month]["total_games"] += 1
        
        if outcome =="loss":
            monthly[month]["total_losses"]+=1
            if game.was_time_loss():
               monthly[month]["time_losses"]+=1 
    for month, data in monthly.items():
        if data["total_losses"] > 0:
            data["time_loss%"] = round(data["time_losses"] / data["total_losses"] * 100, 1)
        else:
            data["time_loss%"] = 0.0

    return monthly

