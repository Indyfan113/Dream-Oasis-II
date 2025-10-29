# bots/ai360_bot.py
import json
import os
from datetime import datetime
from ai_360.ai360_core import AI360

class AI360Bot:
    def __init__(self, ai360: AI360, history_dir="chat_history"):
        self.ai360 = ai360
        self.ai360.initialize()

        # Ensure the directory for history exists
        os.makedirs(history_dir, exist_ok=True)

        # Create a timestamped file for this session
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.history_file = os.path.join(history_dir, f"chat_history_{timestamp}.json")

        # Initialize empty chat history in AI360 memory
        self.ai360.store_memory("chat_history", [])

    def respond(self, message: str) -> str:
        response = self.ai360.process(message)

        # Update in-memory history
        history = self.ai360.recall_memory("chat_history")
        history.append({"user": message, "ai360": response})
        self.ai360.store_memory("chat_history", history)

        # Save current session history to JSON file
        with open(self.history_file, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4)

        return response

    def show_history(self):
        return self.ai360.recall_memory("chat_history") or []
