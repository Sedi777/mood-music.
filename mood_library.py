from __future__ import annotations


APP_NAME = "MoodMix"


def playlist(
    title: str,
    playlist_url: str,
    note: str,
    cover_video_id: str | None = None,
    track_count: int | None = None,
    track_label: str | None = None,
) -> dict:
    return {
        "title": title,
        "playlist_url": playlist_url,
        "note": note,
        "cover_video_id": cover_video_id,
        "track_count": track_count,
        "track_label": track_label,
    }


MOOD_LIBRARY = {
    "happy": {
        "label": "Happy",
        "description": "Bright, catchy playlist picks for a feel-good mood lift.",
        "quotes": [
            "Love is the center of the universe. It can heal anything inside us.",
        ],
        "playlists": [
            playlist(
                "Happy Hit Mix",
                "https://youtube.com/playlist?list=PLOHoVaTp8R7d3L_pjuwIa6nRh4tH5nI4x&si=4Vd_hAyRz1FvdfZY",
                "A full upbeat playlist for happy energy and nonstop pop momentum.",
                track_count=100,
            ),
            playlist(
                "Happy Pop Songs",
                "https://youtube.com/playlist?list=PLos7xCCYivJ94GFKIendd_QA8VW5ElJ6A&si=mfbgT8Sq_xaGcsCn",
                "A second happy mood playlist with pop-focused songs.",
                track_count=100,
            ),
        ],
    },
    "sad": {
        "label": "Sad",
        "description": "Calm, classic, and emotional playlists for quieter moments.",
        "quotes": [
            "The tighter you hold on to someone, the more they want to slip away.",
            "I give myself a good cry if I need it, but then I concentrate on all the good things still in my life.",
            "You may not control all the events that happen to you, but you can decide not to be reduced by them.",
        ],
        "playlists": [
            playlist(
                "Sad Calm Classics I",
                "https://youtube.com/playlist?list=PLP32wGpgzmInrTJp4d7z0WwNg-JCMbIls&si=V-pg5X8QOQBDirpn",
                "A calm classic-style sad playlist for reflective listening.",
                track_count=100,
            ),
            playlist(
                "Sad Calm Classics II",
                "https://youtube.com/playlist?list=PLvFYFNbi-IBG8Y69zkQkCUW4ZLdwUYFNR&si=87EVJYI_8gTtcS09",
                "A second mellow sad playlist with soft emotional flow.",
                track_count=90,
            ),
            playlist(
                "Sad Calm Classics III",
                "https://youtube.com/playlist?list=PL3-sRm8xAzY-v_i64uZfriFSPYHnQd8Vl&si=SarS47xKRmouaadY",
                "A third sad mood playlist for calm, classic, and slower listening.",
                track_count=120,
            ),
        ],
    },
    "focus": {
        "label": "Focus",
        "description": "Steady background playlists for deep work, study, and concentration.",
        "quotes": [
            "Stop letting people who do so little for you control so much of your mind, feelings, and emotions.",
            "People grow through experience if they meet life honestly and courageously. This is how character is built.",
            "If you are not willing to risk the unusual, you will have to settle for the ordinary.",
            "What we fear doing most is usually what we most need to do.",
            "Most of us have two lives: the life we live, and the unlived life within us.",
            "Those who have a why to live can bear almost any how.",
        ],
        "playlists": [
            playlist(
                "Focus Session I",
                "https://youtube.com/playlist?list=PLI6s4sEMQX_Tyt5s5x3QGjoym4Xi4S2XM&si=9F3Hmt32ywKjxg-3",
                "A focused study playlist for concentration and longer sessions.",
                track_count=202,
            ),
            playlist(
                "Focus Session II",
                "https://www.youtube.com/watch?v=OUEBskQuPmg&list=RDOUEBskQuPmg&start_radio=1",
                "A second focus mix that keeps the work session moving.",
                "OUEBskQuPmg",
                track_count=1,
                track_label="Radio mix",
            ),
        ],
    },
    "tired": {
        "label": "Tired",
        "description": "Slow, soft playlists for rest, recovery, and relaxed evenings.",
        "quotes": [
            "Rest is not falling behind. It is how you return to yourself with more strength.",
            "You may not control all the events that happen to you, but you can decide not to be reduced by them.",
        ],
        "playlists": [
            playlist(
                "Tired Reset I",
                "https://youtube.com/playlist?list=PLgzTt0k8mXzH2uOsdGcdS6o_051t_e5B4&si=j24NCyJFR9-qdYyd",
                "A restful playlist for unwinding and slowing the night down.",
                track_count=110,
            ),
            playlist(
                "Tired Reset II",
                "https://youtube.com/playlist?list=PLkVV3IYWRdoB8CnAyQ-MaD4XKnJBbmrgr&si=w9JPXMqwWyBSe3I5",
                "A second tired and relaxing playlist for calm recovery time.",
                track_count=15,
            ),
        ],
    },
}
