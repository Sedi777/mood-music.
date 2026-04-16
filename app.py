from __future__ import annotations

import os
import random

from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


MOOD_LIBRARY = {
    "happy": {
        "label": "Happy",
        "description": "Bright, upbeat songs for a fun mood boost.",
        "songs": [
            {
                "title": "Happy",
                "artist": "Pharrell Williams",
                "url": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
            },
            {
                "title": "Shake It Off",
                "artist": "Taylor Swift",
                "url": "https://www.youtube.com/watch?v=nfWlot6h_JM",
            },
            {
                "title": "Uptown Funk",
                "artist": "Mark Ronson ft. Bruno Mars",
                "url": "https://www.youtube.com/watch?v=OPf0YbXqDm0",
            },
            {
                "title": "Can't Stop the Feeling!",
                "artist": "Justin Timberlake",
                "url": "https://www.youtube.com/watch?v=ru0K8uYEZWw",
            },
        ],
    },
    "sad": {
        "label": "Sad",
        "description": "Gentle songs for when you want to feel understood.",
        "songs": [
            {
                "title": "Someone Like You",
                "artist": "Adele",
                "url": "https://www.youtube.com/watch?v=hLQl3WQQoQ0",
            },
            {
                "title": "Let Her Go",
                "artist": "Passenger",
                "url": "https://www.youtube.com/watch?v=RBumgq5yVrA",
            },
            {
                "title": "All I Want",
                "artist": "Kodaline",
                "url": "https://www.youtube.com/watch?v=mtf7hC17IBM",
            },
            {
                "title": "Stay",
                "artist": "Rihanna ft. Mikky Ekko",
                "url": "https://www.youtube.com/watch?v=JF8BRvqGCNs",
            },
        ],
    },
    "tired": {
        "label": "Tired",
        "description": "Low-pressure picks to relax, focus, or reset.",
        "songs": [
            {
                "title": "Lo-fi Beats",
                "artist": "Lo-fi stream",
                "url": "https://www.youtube.com/watch?v=5qap5aO4i9A",
            },
            {
                "title": "Weightless Relax",
                "artist": "Ambient",
                "url": "https://www.youtube.com/watch?v=UfcAVejslrU",
            },
            {
                "title": "Calm Piano",
                "artist": "Instrumental",
                "url": "https://www.youtube.com/watch?v=1ZYbU82GVz4",
            },
            {
                "title": "Deep Sleep Music",
                "artist": "Relaxation",
                "url": "https://www.youtube.com/watch?v=2OEL4P1Rz04",
            },
        ],
    },
    "angry": {
        "label": "Angry",
        "description": "High-energy tracks to channel strong feelings.",
        "songs": [
            {
                "title": "Lose Yourself",
                "artist": "Eminem",
                "url": "https://www.youtube.com/watch?v=_Yhyp-_hX2s",
            },
            {
                "title": "Stronger",
                "artist": "Kanye West",
                "url": "https://www.youtube.com/watch?v=PsO6ZnUZI0g",
            },
            {
                "title": "Believer",
                "artist": "Imagine Dragons",
                "url": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
            },
            {
                "title": "DNA.",
                "artist": "Kendrick Lamar",
                "url": "https://www.youtube.com/watch?v=NLZRYQMLDW4",
            },
        ],
    },
}


def to_embed_url(video_url: str) -> str:
    video_id = video_url.split("v=")[-1].split("&")[0]
    return f"https://www.youtube.com/embed/{video_id}"


def build_recommendation(mood_key: str) -> dict | None:
    mood = MOOD_LIBRARY.get(mood_key)
    if not mood:
        return None

    track = random.choice(mood["songs"]).copy()
    track["embed_url"] = to_embed_url(track["url"])
    track["mood_key"] = mood_key
    track["mood_label"] = mood["label"]
    track["mood_description"] = mood["description"]
    track["song_count"] = len(mood["songs"])
    return track


@app.route("/", methods=["GET", "POST"])
def index():
    selected_mood = "happy"
    recommendation = build_recommendation(selected_mood)

    if request.method == "POST":
        selected_mood = request.form.get("mood", "happy").lower()
        recommendation = build_recommendation(selected_mood) or recommendation

    mood_cards = [
        {
            "key": mood_key,
            "label": mood["label"],
            "description": mood["description"],
            "count": len(mood["songs"]),
        }
        for mood_key, mood in MOOD_LIBRARY.items()
    ]

    return render_template(
        "index.html",
        mood_cards=mood_cards,
        selected_mood=selected_mood,
        recommendation=recommendation,
    )


@app.get("/api/recommendation")
def api_recommendation():
    mood_key = request.args.get("mood", "happy").lower()
    recommendation = build_recommendation(mood_key)
    if recommendation is None:
        return jsonify({"error": "Unknown mood"}), 404
    return jsonify(recommendation)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
