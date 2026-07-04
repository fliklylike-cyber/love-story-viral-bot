import random
import os
import requests
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *
from scipy.io.wavfile import write

# =============================
# SETUP
# =============================
os.makedirs("output", exist_ok=True)

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

PAGE_ID = "YOUR_FB_PAGE_ID"
PAGE_TOKEN = "YOUR_FB_ACCESS_TOKEN"

# =============================
# STORY ENGINE
# =============================
boys = ["දිනේෂ්", "කවිදු", "අශාන්", "සචින්"]
girls = ["නිශා", "සචිනි", "කාවින්දි", "මධුෂා"]

def generate_story():
    b = random.choice(boys)
    g = random.choice(girls)

    return [
        f"{b} ❤️ {g}",
        "මුලින්ම ඔවුන් හමුවුණේ...",
        "එය ලස්සන ආරම්භයක් වුණා",
        "නමුත් ජීවිතේ ඔවුන්ව වෙන් කළා",
        "හදවතට අමතක වෙන්න බැරි වුණා",
        "අවසානයේ ඔවුන් එකට එක්වුණා ❤️"
    ]

# =============================
# FONT
# =============================
def get_font(size=48):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except:
        return ImageFont.load_default()

# =============================
# BACKGROUND
# =============================
def create_background():
    w, h = 720, 1280
    img = Image.new("RGB", (w, h))
    pixels = img.load()

    for y in range(h):
        for x in range(w):
            r = int(20 + (x/w)*50)
            g = int(10 + (y/h)*40)
            b = int(40 + (x/w)*60)
            pixels[x, y] = (r, g, b)

    return img

# =============================
# SLIDES
# =============================
def create_slides(lines):
    paths = []

    for i, text in enumerate(lines):
        img = create_background()
        draw = ImageDraw.Draw(img)
        font = get_font(50)

        bbox = draw.textbbox((0,0), text, font=font)
        w, h = bbox[2], bbox[3]

        draw.text(((720-w)//2, (1280-h)//2), text, fill="white", font=font)

        path = f"output/slide_{i}.png"
        img.save(path)
        paths.append(path)

    return paths

# =============================
# MUSIC GENERATOR
# =============================
def generate_music(duration=10, filename="output/music.wav"):
    fps = 44100
    t = np.linspace(0, duration, int(fps*duration))

    tone = 0.3*np.sin(2*np.pi*220*t) + 0.2*np.sin(2*np.pi*440*t)
    audio = np.int16(tone * 32767)

    write(filename, fps, audio)
    return filename

# =============================
# VIDEO
# =============================
def create_video(slides):
    clips = []

    for s in slides:
        clip = ImageClip(s).set_duration(2)
        clip = clip.resize(lambda t: 1 + 0.05*t)
        clip = clip.crossfadein(0.5)
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")

    music = generate_music(video.duration)
    audio = AudioFileClip(music)

    video = video.set_audio(audio)

    output = "output/story.mp4"
    video.write_videofile(output, fps=24)

    return output

# =============================
# TELEGRAM
# =============================
def send_telegram(video):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
    with open(video, "rb") as f:
        requests.post(url, data={"chat_id": CHAT_ID}, files={"video": f})

# =============================
# FACEBOOK
# =============================
def post_facebook(video):
    url = f"https://graph.facebook.com/{PAGE_ID}/videos"

    files = {'source': open(video, 'rb')}
    data = {
        'access_token': PAGE_TOKEN,
        'description': "❤️ Sinhala Love Story\n\nFollow for more 💕"
    }

    requests.post(url, files=files, data=data)

# =============================
# RUN
# =============================
def run_once():
    story = generate_story()
    slides = create_slides(story)
    video = create_video(slides)

    send_telegram(video)
    post_facebook(video)

def run_batch(n=2):
    for _ in range(n):
        run_once()

if __name__ == "__main__":
    run_batch(2)
