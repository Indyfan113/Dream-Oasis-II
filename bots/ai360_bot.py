# bots/ai360_bot.py
from ai_360.ai360_core import AI360

class AI360Bot:
    def __init__(self, ai360: AI360):
        self.ai360 = ai360  # use the provided AI360 core instance
    
    def respond(self, message: str) -> str:
        # Simple pass-through to AI360 process
        return self.ai360.process(message)
    
    def show_history(self):
        history = self.ai360.recall_memory("chat_history")
        return history or []
