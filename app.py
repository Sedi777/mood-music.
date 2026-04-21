from __future__ import annotations

import os
import random
from urllib.parse import quote_plus

from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

APP_NAME = "MoodMix"


def song(title: str, artist: str, youtube_id: str | None = None) -> dict:
    query = quote_plus(f"{artist} {title} official")
    url = (
        f"https://www.youtube.com/watch?v={youtube_id}"
        if youtube_id
        else f"https://www.youtube.com/results?search_query={query}"
    )
    return {
        "title": title,
        "artist": artist,
        "url": url,
        "youtube_id": youtube_id,
    }


MOOD_LIBRARY = {
    "happy": {
        "label": "Happy",
        "description": "Big-energy hits, feel-good hooks, and upbeat rap-pop crossovers.",
        "songs": [
            song("Happy", "Pharrell Williams", "ZbZSe6N_BXs"),
            song("Shake It Off", "Taylor Swift", "nfWlot6h_JM"),
            song("Uptown Funk", "Mark Ronson ft. Bruno Mars", "OPf0YbXqDm0"),
            song("Can't Stop the Feeling!", "Justin Timberlake", "ru0K8uYEZWw"),
            song("I Gotta Feeling", "The Black Eyed Peas", "uSD4vsh1zDA"),
            song("Hey Ya!", "OutKast", "PWgvGjAhvIw"),
            song("Can't Hold Us", "Macklemore & Ryan Lewis ft. Ray Dalton", "2zNSgSzhBfM"),
            song("24K Magic", "Bruno Mars", "UqyT8IEBkvY"),
            song("About Damn Time", "Lizzo", "IXXxciRUMzE"),
            song("Good as Hell", "Lizzo", "vuq-VAiW9kw"),
            song("Good Life", "Kanye West ft. T-Pain"),
            song("Good Day", "Nappy Roots"),
            song("Sunflower", "Post Malone & Swae Lee"),
            song("Levitating", "Dua Lipa"),
            song("BIRDS OF A FEATHER", "Billie Eilish"),
        ],
    },
    "confident": {
        "label": "Confident",
        "description": "Main-character tracks for walking in like you already own the room.",
        "songs": [
            song("Run the World (Girls)", "Beyonce", "VBmMU_iwe6U"),
            song("Formation", "Beyonce"),
            song("7 rings", "Ariana Grande"),
            song("Starships", "Nicki Minaj", "SeIJmciN8mo"),
            song("Stronger", "Kanye West", "PsO6ZnUZI0g"),
            song("DNA.", "Kendrick Lamar", "NLZRYQMLDW4"),
            song("POWER", "Kanye West"),
            song("Savage Remix", "Megan Thee Stallion ft. Beyonce"),
            song("Boss Bitch", "Doja Cat"),
            song("Good as Hell", "Lizzo", "vuq-VAiW9kw"),
            song("Money", "Cardi B"),
            song("God's Plan", "Drake"),
        ],
    },
    "chill": {
        "label": "Chill",
        "description": "Soft pop, smooth R&B, and airy songs for an easy mood.",
        "songs": [
            song("Ocean Eyes", "Billie Eilish", "viimfQi_pUw"),
            song("BIRDS OF A FEATHER", "Billie Eilish"),
            song("Sunflower", "Post Malone & Swae Lee"),
            song("Electric Feel", "MGMT"),
            song("Location", "Khalid"),
            song("Snooze", "SZA"),
            song("Stay", "Rihanna ft. Mikky Ekko", "JF8BRvqGCNs"),
            song("telepatia", "Kali Uchis"),
            song("Best Part", "Daniel Caesar ft. H.E.R."),
            song("Peaches", "Justin Bieber ft. Daniel Caesar & Giveon"),
            song("Golden Hour", "JVKE"),
            song("Pink + White", "Frank Ocean"),
        ],
    },
    "sad": {
        "label": "Sad",
        "description": "Heartfelt songs for crying, healing, and feeling understood.",
        "songs": [
            song("Someone Like You", "Adele", "hLQl3WQQoQ0"),
            song("Let Her Go", "Passenger", "RBumgq5yVrA"),
            song("All I Want", "Kodaline", "mtf7hC17IBM"),
            song("drivers license", "Olivia Rodrigo"),
            song("Lovely", "Billie Eilish & Khalid"),
            song("Happier", "Ed Sheeran"),
            song("When the Party's Over", "Billie Eilish"),
            song("Traitor", "Olivia Rodrigo"),
            song("Easy On Me", "Adele"),
            song("Glimpse of Us", "Joji"),
            song("Heather", "Conan Gray"),
            song("Skinny Love", "Bon Iver"),
        ],
    },
    "tired": {
        "label": "Tired",
        "description": "Gentle music for late nights, quiet mornings, and mental reset time.",
        "songs": [
            song("Lo-fi Beats", "Lo-fi stream", "5qap5aO4i9A"),
            song("Weightless Relax", "Ambient", "UfcAVejslrU"),
            song("Calm Piano", "Instrumental", "1ZYbU82GVz4"),
            song("Deep Sleep Music", "Relaxation", "2OEL4P1Rz04"),
            song("Lovely", "Billie Eilish & Khalid"),
            song("Come Away With Me", "Norah Jones"),
            song("Holocene", "Bon Iver"),
            song("Bloom", "The Paper Kites"),
            song("Night Trouble", "Petit Biscuit"),
            song("Saturn", "SZA"),
            song("Moon Song", "Phoebe Bridgers"),
            song("Slow Burn", "Kacey Musgraves"),
        ],
    },
    "angry": {
        "label": "Angry",
        "description": "Heavy momentum, sharp drums, and bold rap for high-intensity moods.",
        "songs": [
            song("Lose Yourself", "Eminem", "_Yhyp-_hX2s"),
            song("Believer", "Imagine Dragons", "7wtfhZwyrcc"),
            song("DNA.", "Kendrick Lamar", "NLZRYQMLDW4"),
            song("SICKO MODE", "Travis Scott"),
            song("POWER", "Kanye West"),
            song("HUMBLE.", "Kendrick Lamar"),
            song("Till I Collapse", "Eminem"),
            song("Black Skinhead", "Kanye West"),
            song("N95", "Kendrick Lamar"),
            song("X Gon' Give It To Ya", "DMX"),
            song("Remember the Name", "Fort Minor"),
            song("Can't Be Touched", "Roy Jones Jr."),
        ],
    },
    "romantic": {
        "label": "Romantic",
        "description": "Warm, dreamy songs for crushes, dates, and soft-heart moments.",
        "songs": [
            song("Perfect", "Ed Sheeran"),
            song("Adore You", "Harry Styles"),
            song("Best Part", "Daniel Caesar ft. H.E.R."),
            song("All of Me", "John Legend"),
            song("Love on the Brain", "Rihanna"),
            song("Die With A Smile", "Lady Gaga & Bruno Mars"),
            song("Until I Found You", "Stephen Sanchez"),
            song("Can I Call You Rose?", "Thee Sacred Souls"),
            song("Earned It", "The Weeknd"),
            song("Love Galore", "SZA ft. Travis Scott"),
            song("Teenage Dream", "Katy Perry"),
            song("Love Me Like You Do", "Ellie Goulding"),
        ],
    },
    "focus": {
        "label": "Focus",
        "description": "Clean, steady songs and mellow beats for studying or getting work done.",
        "songs": [
            song("Lo-fi Beats", "Lo-fi stream", "5qap5aO4i9A"),
            song("Sunset Lover", "Petit Biscuit"),
            song("Midnight City", "M83"),
            song("Innerbloom", "RUFUS DU SOL"),
            song("Nights", "Frank Ocean"),
            song("After Dark", "Mr.Kitty"),
            song("Intro", "The xx"),
            song("Space Song", "Beach House"),
            song("Get You The Moon", "Kina ft. Snow"),
            song("Young and Beautiful", "Lana Del Rey"),
            song("See You Again", "Tyler, The Creator ft. Kali Uchis"),
            song("Money Trees", "Kendrick Lamar ft. Jay Rock"),
        ],
    },
}


def to_embed_url(song_data: dict) -> str | None:
    youtube_id = song_data.get("youtube_id")
    if not youtube_id:
        return None
    return f"https://www.youtube.com/embed/{youtube_id}"


def build_recommendation(mood_key: str) -> dict | None:
    mood = MOOD_LIBRARY.get(mood_key)
    if not mood:
        return None

    track = random.choice(mood["songs"]).copy()
    track["embed_url"] = to_embed_url(track)
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
