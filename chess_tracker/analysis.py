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


