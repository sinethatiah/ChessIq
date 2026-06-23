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
