from engine.scoring import score
from engine.verdict import verdict

def analyze_business(data):
    s = score(data)
    v = verdict(data, s)
    return {
        "score": s,
        "verdict": v
    }
