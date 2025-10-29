# ai_360/ai360_core.py
import json
from datetime import datetime

class AI360:
    def __init__(self):
        self.status = "Not initialized"
        self.memory = {}
        self.bots = []

    def initialize(self):
        self.status = "AI-360 initialized"
        print("AI-360 module initialized")

    def add_bot(self, bot):
        self.bots.append(bot)
        print(f"Bot '{bot.__class__.__name__}' added to AI-360")

    def store_memory(self, key, value):
        self.memory[key] = value
        print(f"Memory stored: {key} -> {value}")

    def recall_memory(self, key):
        return self.memory.get(key, None)

    def process(self, message: str) -> str:
        # simple keyword-based responses
        message_lower = message.lower()
        if "hello" in message_lower:
            return "Hello! AI-360 here."
        elif "how are you" in message_lower:
            return "I am running smoothly!"
        elif "time" in message_lower:
            return f"The current time is {datetime.now().strftime('%H:%M:%S')}"
        else:
            return f"AI-360 processed: {message}"

    def system_status(self):
        print(f"Status: {self.status}, Bots connected: {len(self.bots)}")
        for bot in self.bots:
            print(f" - {bot.__class__.__name__}")
