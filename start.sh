#!/usr/bin/env bash

if [ $# -lt 1 ]; then
  echo "Usage: ./start.sh <PORT>"
  exit 1
fi

PORT=$1

if docker compose version > /dev/null 2>&1; then
  PORT=$PORT docker compose up --build -d
else
  PORT=$PORT docker-compose up --build -d
fi

echo "App is running at http://localhost:${PORT}"