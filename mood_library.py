from __future__ import annotations


APP_NAME = "MoodMix"


def playlist(title: str, playlist_url: str, note: str, cover_video_id: str | None = None) -> dict:
    return {
        "title": title,
        "playlist_url": playlist_url,
        "note": note,
        "cover_video_id": cover_video_id,
    }


MOOD_LIBRARY = {
    "happy": {
        "label": "Happy",
        "description": "Bright, catchy playlist picks for a feel-good mood lift.",
        "quote": "Love is the center of the universe. It can heal anything inside us.",
        "playlists": [
            playlist(
                "Happy Hit Mix",
                "https://youtube.com/playlist?list=PLOHoVaTp8R7d3L_pjuwIa6nRh4tH5nI4x&si=4Vd_hAyRz1FvdfZY",
                "A full upbeat playlist for happy energy and nonstop pop momentum.",
            ),
            playlist(
                "Happy Pop Songs",
                "https://youtube.com/playlist?list=PLos7xCCYivJ94GFKIendd_QA8VW5ElJ6A&si=mfbgT8Sq_xaGcsCn",
                "A second happy mood playlist with pop-focused songs.",
            ),
        ],
    },
    "sad": {
        "label": "Sad",
        "description": "Calm, classic, and emotional playlists for quieter moments.",
        "quote": "The tighter you hold on to someone, the more they want to slip away.",
        "playlists": [
            playlist(
                "Sad Calm Classics I",
                "https://youtube.com/playlist?list=PLP32wGpgzmInrTJp4d7z0WwNg-JCMbIls&si=V-pg5X8QOQBDirpn",
                "A calm classic-style sad playlist for reflective listening.",
            ),
            playlist(
                "Sad Calm Classics II",
                "https://youtube.com/playlist?list=PLvFYFNbi-IBG8Y69zkQkCUW4ZLdwUYFNR&si=87EVJYI_8gTtcS09",
                "A second mellow sad playlist with soft emotional flow.",
            ),
            playlist(
                "Sad Calm Classics III",
                "https://youtube.com/playlist?list=PL3-sRm8xAzY-v_i64uZfriFSPYHnQd8Vl&si=SarS47xKRmouaadY",
                "A third sad mood playlist for calm, classic, and slower listening.",
            ),
        ],
    },
    "focus": {
        "label": "Focus",
        "description": "Steady background playlists for deep work, study, and concentration.",
        "quote": "Small steady steps still build something beautiful. Keep your mind where your future is.",
        "playlists": [
            playlist(
                "Focus Session I",
                "https://youtube.com/playlist?list=PLI6s4sEMQX_Tyt5s5x3QGjoym4Xi4S2XM&si=9F3Hmt32ywKjxg-3",
                "A focused study playlist for concentration and longer sessions.",
            ),
            playlist(
                "Focus Session II",
                "https://www.youtube.com/watch?v=OUEBskQuPmg&list=RDOUEBskQuPmg&start_radio=1",
                "A second focus mix that keeps the work session moving.",
                "OUEBskQuPmg",
            ),
        ],
    },
    "tired": {
        "label": "Tired",
        "description": "Slow, soft playlists for rest, recovery, and relaxed evenings.",
        "quote": "Rest is not falling behind. It is how you return to yourself with more strength.",
        "playlists": [
            playlist(
                "Tired Reset I",
                "https://youtube.com/playlist?list=PLgzTt0k8mXzH2uOsdGcdS6o_051t_e5B4&si=j24NCyJFR9-qdYyd",
                "A restful playlist for unwinding and slowing the night down.",
            ),
            playlist(
                "Tired Reset II",
                "https://youtube.com/playlist?list=PLkVV3IYWRdoB8CnAyQ-MaD4XKnJBbmrgr&si=w9JPXMqwWyBSe3I5",
                "A second tired and relaxing playlist for calm recovery time.",
            ),
        ],
    },
}
