## Mini RAG App

Small FastAPI service with a single welcome endpoint. This is a minimal scaffold you can extend with retrieval and generation features.

## Requirements

- Python 3.10+

## Setup

```bash
python -m venv .venv
```

Activate the environment:

```bash
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# WSL / Linux
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## Endpoints

- `GET /` -> `{ "message": "Welcome to the Mini RAG App!" }`

Example:

```bash
curl http://127.0.0.1:5000/
```

## Notes for Windows + WSL

If you run the server in WSL and want to call it from Windows (Postman), enable localhost forwarding:

1. Create or edit `%USERPROFILE%\.wslconfig`:
	```
	[wsl2]
	localhostForwarding=true
	```
2. Restart WSL:
	```powershell
	wsl --shutdown
	```

Then use `http://localhost:5000/` from Windows.
