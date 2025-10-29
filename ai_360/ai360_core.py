# ai_360/ai360_core.py
import json
import os

class AI360:
    def __init__(self, memory_file="ai360_memory.json"):
        self.status = "Not initialized"
        self.memory_file = memory_file
        self.memory = self.load_memory()
        self.bots = []

    def initialize(self):
        self.status = "AI-360 initialized"
        print("AI-360 module initialized")

    def add_bot(self, bot):
        self.bots.append(bot)
        print(f"Bot '{bot.__class__.__name__}' added to AI-360")

    def store_memory(self, key, value):
        self.memory[key] = value
        self.save_memory()
        print(f"Memory stored: {key} -> {value}")

    def recall_memory(self, key):
        return self.memory.get(key, None)

    def process(self, message: str) -> str:
        message_lower = message.lower()
        if "hello" in message_lower:
            return "Hello! AI-360 here."
        elif "how are you" in message_lower:
            return "I am running smoothly!"
        elif "time" in message_lower:
            from datetime import datetime
            return f"The current time is {datetime.now().strftime('%H:%M:%S')}"
        else:
            return f"AI-360 processed: {message}"

    def system_status(self):
        print(f"Status: {self.status}, Bots connected: {len(self.bots)}")
        for bot in self.bots:
            print(f" - {bot.__class__.__name__}")

    # Persistent memory helpers
    def save_memory(self):
        try:
            with open(self.memory_file, "w", encoding="utf-8") as f:
                json.dump(self.memory, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error saving memory: {e}")

    def load_memory(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading memory: {e}")
        return {}
