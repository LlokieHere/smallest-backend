# Smallest Backend

A minimal Flask server with JSON endpoints, built as part of backend engineering internship training.

## Endpoints
- `GET /` — health check message
- `GET /health` — server status
- `GET /about` — intern name and role
- `GET /contact` — intern email and LinkedIn

## Setup
1. Clone this repo
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/Scripts/activate` (Windows Git Bash) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install flask`
5. Run the server: `python app.py`
6. Visit `http://127.0.0.1:5000/`
