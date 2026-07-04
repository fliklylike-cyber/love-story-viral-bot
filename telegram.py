import requests

BOT_TOKEN = "PUT_YOUR_TOKEN"
CHAT_ID = "PUT_YOUR_CHAT_ID"

def send(video):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"

    with open(video, "rb") as f:
        requests.post(url, data={"chat_id": CHAT_ID}, files={"video": f})
