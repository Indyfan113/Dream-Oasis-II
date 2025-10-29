#!/usr/bin/env bash
# run_ai360_chat.sh — Launch AI-360 kernel and chat window

echo ">>> Starting AI-360 Kernel..."
/c/Users/hdick/AppData/Local/Programs/Python/Python314/python.exe -m core.main_kernel

echo ">>> Starting AI-360 Chat Window..."
/c/Users/hdick/AppData/Local/Programs/Python/Python314/python.exe -m core.chat_window
