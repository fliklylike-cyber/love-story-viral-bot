import random

boys = ["දිනේෂ්", "කවිදු", "අශාන්", "සචින්"]
girls = ["නිශා", "සචිනි", "කාවින්දි", "මධුෂා"]

openings = [
    "මුලින්ම ඔවුන් හමුවුණේ...",
    "ඔවුන්ගේ කතාව ආරම්භ වුණේ...",
]

conflicts = [
    "නමුත් ජීවිතේ ඔවුන්ව වෙන් කළා",
    "ඒ ආදරයට බාධා ආවා",
]

emotions = [
    "ආදරය තවමත් තිබුණා",
    "හදවතට අමතක වෙන්න බැරි වුණා",
]

endings = [
    "අවසානයේ ඔවුන් එකට එක්වුණා ❤️",
    "ආදරය ජය ගත්තා 💕",
    "එය අමතක නොවන ආදරයක් වුණා ✨"
]

def generate_story():
    b = random.choice(boys)
    g = random.choice(girls)

    return [
        f"{b} ❤️ {g}",
        random.choice(openings),
        "එය ලස්සන ආරම්භයක් වුණා",
        random.choice(conflicts),
        random.choice(emotions),
        random.choice(endings)
    ]
