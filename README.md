# Mood Music

This project now includes a shareable web app version of the mood music generator.

## Run locally

1. Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the app:

```bash
flask --app app run
```

4. Open the local URL shown in your terminal.

## Share with other users

You can deploy this app to services like Render or Railway.

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app --bind 0.0.0.0:$PORT`

The included `Procfile` makes deployment easier on platforms that support it.

## Existing desktop app

The original Tkinter version is still available in `mood_app.py`.
