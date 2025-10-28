# First kernel for Oasis II

from bots.helper_bot import HelperBot
from ai_360.ai360_core import AI360

def initialize_system():
    print("Oasis II system initialized")

if __name__ == "__main__":
    initialize_system()
    
    # Initialize AI-360
    ai360 = AI360()
    ai360.initialize()

    # Initialize HelperBot and register it
    bot = HelperBot()
    ai360.add_bot(bot)
    print(bot.greet())

    # Optional: show system status
    ai360.system_status()
