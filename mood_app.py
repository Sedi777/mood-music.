import tkinter as tk
import random
import webbrowser

# ---------- Window ----------
root = tk.Tk()
root.title("Mood Music Pro 🎧")
root.geometry("500x550")
root.configure(bg="#121212")

# ---------- Title ----------
title = tk.Label(
    root,
    text="🎧 Mood Music Pro",
    font=("Helvetica", 22, "bold"),
    fg="#00ffcc",
    bg="#121212"
)
title.pack(pady=15)

subtitle = tk.Label(
    root,
    text="Choose your mood and vibe 🎶",
    font=("Helvetica", 12),
    fg="white",
    bg="#121212"
)
subtitle.pack(pady=5)

# ---------- Result ----------
result = tk.StringVar()
result_label = tk.Label(
    root,
    textvariable=result,
    wraplength=400,
    font=("Helvetica", 12),
    fg="#dddddd",
    bg="#121212"
)
result_label.pack(pady=20)

# ---------- SONG DATABASE (expandable) ----------

happy_songs = [
    ("Happy - Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
    ("Shake It Off - Taylor Swift", "https://www.youtube.com/watch?v=nfWlot6h_JM"),
    ("Uptown Funk - Bruno Mars", "https://www.youtube.com/watch?v=OPf0YbXqDm0"),
    ("Can’t Stop the Feeling - Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw"),
    ("Best Day Of My Life - American Authors", "https://www.youtube.com/watch?v=Y66j_BUCBMY"),
]

sad_songs = [
    ("Someone Like You - Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
    ("Let Her Go - Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA"),
    ("All I Want - Kodaline", "https://www.youtube.com/watch?v=mtf7hC17IBM"),
    ("Stay - Rihanna", "https://www.youtube.com/watch?v=JF8BRvqGCNs"),
    ("Happier - Ed Sheeran", "https://www.youtube.com/watch?v=iWZmdoY1aTE"),
]

tired_songs = [
    ("Lo-fi Beats", "https://www.youtube.com/watch?v=5qap5aO4i9A"),
    ("Weightless Relax", "https://www.youtube.com/watch?v=UfcAVejslrU"),
    ("Calm Piano", "https://www.youtube.com/watch?v=1ZYbU82GVz4"),
    ("Deep Sleep Music", "https://www.youtube.com/watch?v=2OEL4P1Rz04"),
]

angry_songs = [
    ("Lose Yourself - Eminem", "https://www.youtube.com/watch?v=_Yhyp-_hX2s"),
    ("Stronger - Kanye West", "https://www.youtube.com/watch?v=PsO6ZnUZI0g"),
    ("Believer - Imagine Dragons", "https://www.youtube.com/watch?v=7wtfhZwyrcc"),
    ("DNA - Kendrick Lamar", "https://www.youtube.com/watch?v=NLZRYQMLDW4"),
]

# ---------- FUNCTION ----------
def play_music(song_list):
    song = random.choice(song_list)
    result.set(f"🎵 {song[0]}\nOpening YouTube...")
    webbrowser.open(song[1])

# ---------- HOVER EFFECT ----------
def on_enter(e):
    e.widget['background'] = "#00ffcc"

def on_leave(e, color):
    e.widget['background'] = color

# ---------- BUTTON MAKER ----------
def create_button(text, color, songs):
    btn = tk.Button(
        root,
        text=text,
        bg=color,
        fg="black",
        font=("Helvetica", 13, "bold"),
        width=20,
        height=2,
        bd=0,
        command=lambda: play_music(songs)
    )
    btn.pack(pady=10)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", lambda e: on_leave(e, color))

# ---------- BUTTONS ----------
create_button("Happy 😄", "#f6c90e", happy_songs)
create_button("Sad 😢", "#6ab04c", sad_songs)
create_button("Tired 😴", "#a29bfe", tired_songs)
create_button("Angry 😡", "#eb4d4b", angry_songs)

# ---------- RUN ----------
root.mainloop()

