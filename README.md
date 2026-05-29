# API Bridge Builder

> Autonomous API bridge builder with NL parsing and Ralph self-critique loop. Describe two systems to connect and get a structured bridge spec.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/skippersayshi/api-bridge-builder)

## Features

- Natural language → field mapping spec
- SQLite knowledge base for reuse across sessions  
- Ralph loop: build → critique → retry until optimal
- REST API + Apple-style web UI

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
# Open http://localhost:8000
```

## Deploy

Click the Railway button above — `railway.toml` is pre-configured.
