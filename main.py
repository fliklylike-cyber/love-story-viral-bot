from stories import generate_story
from video import create_slides, create_video
from telegram import send
from facebook import post

def run_once():
    story = generate_story()

    slides = create_slides(story)
    video = create_video(slides)

    send(video)
    post(video)

def run_batch(n=5):
    for _ in range(n):
        run_once()

if __name__ == "__main__":
    run_batch(3)  # number of videos
