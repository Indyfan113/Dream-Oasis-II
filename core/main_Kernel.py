# First kernel for Oasis II
def initialize_system():
	print("Oasis II system initialized")
if __name__ == "__main__":
	initialize_system()
from bots.helper_bot import HelperBot

if __name__ == "__main__":
    bot = HelperBot()
    print(bot.greet())
