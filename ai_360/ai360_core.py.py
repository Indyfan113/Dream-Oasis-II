# ai_360/ai360_core.py

class AI360:
    def __init__(self):
        self.status = "Not initialized"
        self.memory = {}   # Store key system states
        self.bots = []     # Track connected bots

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

    def system_status(self):
        print(f"Status: {self.status}, Bots connected: {len(self.bots)}")
