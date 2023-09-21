#!/bin/bash
echo "🟡 starting NGROK"
ngrok http app:8000 &
sleep 5

public_url=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')
echo "✅ Public NGROK url initialized: $public_url"

wait %1