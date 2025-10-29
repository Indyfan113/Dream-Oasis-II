#!/usr/bin/env bash
# scripts/start_oasis.sh — Launch full Oasis II + AI-360 system

echo ">>> Starting full Oasis II + AI-360 system..."

# 1. Run the main kernel (initializes system & AI-360)
python -m core.main_kernel

# 2. Run the chat window (start interactive bots)
python -m core.chat_window
