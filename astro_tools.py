
import requests

def get_daily_horoscope(sign: str) -> str:
    url = f"https://aztro.sameerkumar.website/?sign={sign.lower()}&day=today"
    response = requests.post(url)
    data = response.json()
    return f"{data['description']}\nMood: {data['mood']}, Lucky color: {data['color']}"
