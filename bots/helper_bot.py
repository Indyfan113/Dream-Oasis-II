# HelperBot module 
# helper_bot.py

# bots/helper_bot.py
class HelperBot:
    def greet(self):
        return "HelperBot: System check complete. Standing by for tasks."

    def receive(self, message):
        response = f"HelperBot received: {message}"
        return response
