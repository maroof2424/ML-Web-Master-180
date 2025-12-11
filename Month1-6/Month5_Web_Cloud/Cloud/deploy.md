# Deployment Guide (Render)

## Start Command
uvicorn app.main:app --host 0.0.0.0 --port 10000

## Health Check
/ping or /health

## Environment Variables
MODEL_PATH=model.pkl
