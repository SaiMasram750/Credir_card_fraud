#!/bin/bash
echo "🚀 Starting Shield.OS Backend Server..."
python -m uvicorn backend.app:app --host 127.0.0.1 --port 8000 --reload
