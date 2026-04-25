#!/usr/bin/env bash

if [$# -lt 1]; then
    echo "Usage: ./start.sh <PORT>"
    exit 1
fi

PORT=$1

PORT=$PORT docker compose up --build -d 
echo "Aplikacja dziala na http://localhost:${PORT}"