# FD AI 0.2

FD AI 0.2 is a clean starter application based on the agreed architecture:

- Router receives and analyzes user requests.
- Tool Manager manages available tools.
- Module Manager manages application modules.
- Version Manager exposes the current version and upgrade path.
- Assets contains the FD AI logo.
- The project is intentionally simple so it can be extended toward FD AI 0.5, 1.0 and 5.0.

## Run locally

```bash
pip install -r requirements.txt
python main.py
```

Then open `http://localhost:5000`.

## Render

Use:
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn main:app`

The project uses the `PORT` environment variable supplied by Render.

## Important

This ZIP is the **source application project**, not an Android APK. It is designed to be uploaded to GitHub first and then deployed to a Python-capable service such as Render.
