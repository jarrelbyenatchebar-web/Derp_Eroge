#!/bin/bash

git status
git add .

echo "============================"

git status

if [ -z "$1" ]; then
  echo "❌ Commit message required"
  echo "Usage: ./commit.sh \"your message\""
  exit 1
fi

git commit -m "$1"
git push origin main