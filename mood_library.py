from __future__ import annotations


APP_NAME = "MoodMix"


def playlist(title: str, youtube_id: str, note: str, playlist_url: str | None = None) -> dict:
    return {
        "title": title,
        "youtube_id": youtube_id,
        "note": note,
        "playlist_url": playlist_url,
    }


MOOD_LIBRARY = {
    "happy": {
        "label": "Happy",
        "description": "Upbeat pop and bright energy from your curated YouTube picks.",
        "playlists": [
            playlist(
                "Happy Playlist 1",
                "ko70cExuzZM",
                "Your first happy playlist pick for feel-good energy.",
            ),
            playlist(
                "Happy Pop Songs",
                "ekr2nIex040",
                "A pop-focused happy playlist from your links.",
            ),
            playlist(
                "Happy Playlist 3",
                "htk6MRjmcnQ",
                "Another upbeat happy mix from your saved YouTube playlists.",
            ),
        ],
    },
    "sad": {
        "label": "Sad",
        "description": "Calm and classic-leaning playlists for soft, emotional moods.",
        "playlists": [
            playlist(
                "Sad Calm Classics 1",
                "K3Qzzggn--s",
                "A calm and classic sad playlist from your YouTube selection.",
            ),
            playlist(
                "Sad Calm Classics 2",
                "Jkj36B1YuDU",
                "A second mellow sad playlist for a gentler mood.",
            ),
        ],
    },
    "focus": {
        "label": "Focus",
        "description": "Steady background playlists for studying, reading, and concentration.",
        "playlists": [
            playlist(
                "Focus Playlist 1",
                "u2ah9tWTkmk",
                "Your first focus playlist for study and concentration.",
            ),
            playlist(
                "Focus Playlist 2",
                "tpWLeUt_7Cc",
                "A second focus mix for longer work sessions.",
            ),
        ],
    },
    "tired": {
        "label": "Tired",
        "description": "Quiet reset playlists for late nights, rest, and slow mornings.",
        "playlists": [
            playlist(
                "Tired Reset 1",
                "RoxiLsgSCJA",
                "A soft tired-mood playlist for unwinding.",
            ),
            playlist(
                "Tired Reset 2",
                "__UV4QRnkps",
                "A second calming playlist for rest and recovery.",
            ),
            playlist(
                "Tired Reset 3",
                "ujAXBVfAlUY",
                "Another gentle tired playlist from your YouTube picks.",
            ),
        ],
    },
}
