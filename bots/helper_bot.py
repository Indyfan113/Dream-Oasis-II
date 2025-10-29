# HelperBot module 
# helper_bot.py

class HelperBot:
    def __init__(self):
        self.name = "HelperBot"

    def greet(self):
        return f"{self.name}: System check complete. Standing by for tasks."

    def receive(self, message):
        # Simple echo logic for now
        return f"{self.name} received: {message}"
