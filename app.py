from __future__ import annotations

import os
import random
from urllib.parse import quote_plus

from flask import Flask, jsonify, render_template, request

from mood_library import APP_NAME, MOOD_LIBRARY


app = Flask(__name__)


def youtube_watch_url(video_id: str | None, title: str, artist: str) -> str:
    if video_id:
        return f"https://www.youtube.com/watch?v={video_id}"
    query = quote_plus(f"{artist} {title} official")
    return f"https://www.youtube.com/results?search_query={query}"


def youtube_embed_url(video_id: str) -> str:
    return f"https://www.youtube.com/embed/{video_id}"


def youtube_art_url(video_id: str) -> str:
    return f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"


def build_recommendation(mood_key: str) -> dict | None:
    mood = MOOD_LIBRARY.get(mood_key)
    if not mood:
        return None

    fallback_video_id = mood["fallback_video_id"]
    track = random.choice(mood["songs"]).copy()
    active_video_id = track.get("youtube_id") or fallback_video_id

    track["url"] = youtube_watch_url(track.get("youtube_id"), track["title"], track["artist"])
    track["embed_url"] = youtube_embed_url(active_video_id)
    track["art_url"] = youtube_art_url(active_video_id)
    track["mood_key"] = mood_key
    track["mood_label"] = mood["label"]
    track["mood_description"] = mood["description"]
    track["song_count"] = len(mood["songs"])
    track["has_exact_video"] = bool(track.get("youtube_id"))
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

    total_tracks = sum(len(mood["songs"]) for mood in MOOD_LIBRARY.values())

    return render_template(
        "index.html",
        app_name=APP_NAME,
        mood_cards=mood_cards,
        selected_mood=selected_mood,
        recommendation=recommendation,
        total_moods=len(MOOD_LIBRARY),
        total_tracks=total_tracks,
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
