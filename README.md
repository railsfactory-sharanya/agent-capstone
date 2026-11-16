# Harbor support triage

A Python program that triages support tickets for Harbor, a fictional hosted team wiki. Part 1 is the database and a check that the Gemini key works.

The model is called with the Google Gen AI SDK (`google-genai`). The key stays in `.env` as `GEMINI_API_KEY`.

## Setup

Python 3.11 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Part 1

```bash
python check_key.py
python seed.py
```

`check_key.py` prints one sentence from `gemini-3.5-flash`, then the token counts for that call. `seed.py` deletes `data/support.db` if it is already there and builds it again: 15 customers, 50 tickets, 32 resolved-history rows.
