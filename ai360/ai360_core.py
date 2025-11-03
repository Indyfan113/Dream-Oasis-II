import json
import os
from datetime import datetime

print("DEBUG: ai360_core.py is executing")  # always prints first

class AI360:
    def __init__(self, memory_file="ai360_memory.json"):
        self.status = "Not initialized"
        self.memory_file = memory_file
        self.memory = self.load_memory()
        self.bots = []

    def main(self, session_config=None):
        print("✅ AI-360 Kernel started in sandbox mode!")
        self.initialize()
        for i in range(3):
            print(f"Sandbox loop iteration {i+1}")

    def initialize(self):
        self.status = "AI-360 initialized"
        print("AI-360 module initialized")

    def load_memory(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading memory: {e}")
        return {}

if __name__ == "__main__":
    test_config = {'personas': ['default'], 'api_config': {}}
    ai = AI360()
    ai.main(test_config)
