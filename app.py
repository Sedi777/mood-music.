from __future__ import annotations

import os

from flask import Flask, jsonify, render_template, request

from mood_library import APP_NAME, MOOD_LIBRARY


app = Flask(__name__)


def youtube_watch_url(video_id: str) -> str:
    return f"https://www.youtube.com/watch?v={video_id}"


def youtube_embed_url(video_id: str) -> str:
    return f"https://www.youtube.com/embed/{video_id}"


def youtube_art_url(video_id: str) -> str:
    return f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"


def build_recommendation(mood_key: str, playlist_index: int = 0) -> dict | None:
    mood = MOOD_LIBRARY.get(mood_key)
    if not mood:
        return None

    playlists = mood["playlists"]
    safe_index = max(0, min(playlist_index, len(playlists) - 1))
    current = playlists[safe_index].copy()
    current["url"] = youtube_watch_url(current["youtube_id"])
    current["embed_url"] = youtube_embed_url(current["youtube_id"])
    current["art_url"] = youtube_art_url(current["youtube_id"])
    current["mood_key"] = mood_key
    current["mood_label"] = mood["label"]
    current["mood_description"] = mood["description"]
    current["playlist_count"] = len(playlists)
    current["playlist_index"] = safe_index
    return current


@app.route("/", methods=["GET", "POST"])
def index():
    selected_mood = "happy"
    selected_playlist_index = 0

    if request.method == "POST":
        selected_mood = request.form.get("mood", "happy").lower()
        selected_playlist_index = int(request.form.get("playlist_index", "0"))

    recommendation = build_recommendation(selected_mood, selected_playlist_index)

    mood_cards = [
        {
            "key": mood_key,
            "label": mood["label"],
            "description": mood["description"],
            "count": len(mood["playlists"]),
        }
        for mood_key, mood in MOOD_LIBRARY.items()
    ]

    total_playlists = sum(len(mood["playlists"]) for mood in MOOD_LIBRARY.values())
    active_playlists = MOOD_LIBRARY[selected_mood]["playlists"]

    return render_template(
        "index.html",
        app_name=APP_NAME,
        mood_cards=mood_cards,
        selected_mood=selected_mood,
        recommendation=recommendation,
        total_moods=len(MOOD_LIBRARY),
        total_playlists=total_playlists,
        active_playlists=active_playlists,
    )


@app.get("/api/recommendation")
def api_recommendation():
    mood_key = request.args.get("mood", "happy").lower()
    playlist_index = int(request.args.get("playlist_index", "0"))
    recommendation = build_recommendation(mood_key, playlist_index)
    if recommendation is None:
        return jsonify({"error": "Unknown mood"}), 404
    return jsonify(recommendation)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
