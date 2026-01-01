from fastapi import FastAPI, Header, HTTPException
from engine.intake import analyze_business

app = FastAPI()

SECRET = "YOUR_PRIVATE_KEY"

@app.post("/analyze")
def analyze(data: dict, authorization: str = Header(None)):
    if authorization != f"Bearer {SECRET}":
        raise HTTPException(status_code=401)

    return analyze_business(data)
