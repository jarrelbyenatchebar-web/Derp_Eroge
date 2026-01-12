#!/bin/bash

echo "📡 Fetching remote updates..."
git fetch

echo "============================"
echo "🔍 Checking status..."
git status

echo "============================"
echo "⬇️ Pulling latest changes..."
git pull --ff-only

echo "============================"
echo "✅ Update complete."
