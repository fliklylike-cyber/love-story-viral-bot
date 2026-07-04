import requests

PAGE_ID = "PUT_PAGE_ID"
TOKEN = "PUT_PAGE_ACCESS_TOKEN"

def post(video):
    url = f"https://graph.facebook.com/{PAGE_ID}/videos"

    files = {'source': open(video, 'rb')}
    data = {
        'access_token': TOKEN,
        'description': "❤️ Sinhala Love Story\n\nFollow for more 💕"
    }

    requests.post(url, files=files, data=data)
