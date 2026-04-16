import keyboard
import os

def open_app():
    # This will run your mood app when hotkey is pressed
    os.system("python3 mood_app.py")

# Set hotkey: S + 7
keyboard.add_hotkey('s+7', open_app)

print("Press S + 7 to open Mood Music App...")
keyboard.wait()  # Wait forever until program closes