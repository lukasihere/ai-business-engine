def score(data):
    score = 0

    if data["budget"] < 1000:
        score -= 30

    if data["market_size"] == "small":
        score -= 20

    if data["experience"] == "none":
        score -= 25

    if data["expectation"] == "get rich fast":
        score -= 40

    return score
