from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *

FONT_PATH = "fonts/sinhala.ttf"

def create_slides(lines):
    paths = []

    for i, text in enumerate(lines):
        img = Image.new("RGB", (720, 1280), (15, 15, 40))
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype(FONT_PATH, 50)

        bbox = draw.textbbox((0,0), text, font=font)
        w, h = bbox[2], bbox[3]

        draw.text(((720-w)//2, (1280-h)//2), text, fill="white", font=font)

        path = f"output/slide_{i}.png"
        img.save(path)
        paths.append(path)

    return paths


def create_video(slides):
    clips = []

    for s in slides:
        clip = ImageClip(s).set_duration(2)
        clip = clip.resize(lambda t: 1 + 0.05*t)
        clip = clip.crossfadein(0.5)
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")

    audio = AudioFileClip("music.mp3").subclip(0, video.duration)
    video = video.set_audio(audio)

    out = "output/story.mp4"
    video.write_videofile(out, fps=24)

    return out
