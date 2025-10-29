# run_all_bots.py (snippet)
from ai_360.ai360_core import AI360
from bots.helper_bot import HelperBot
from bots.ai360_bot import AI360Bot

def main():
    print(">>> Starting full Oasis II + AI-360 system...")

    ai360 = AI360()
    ai360.initialize()

    # Initialize HelperBot
    helper_bot = HelperBot()
    ai360.add_bot(helper_bot)

    # Initialize AI360Bot
    ai360_bot = AI360Bot(ai360)  # <-- pass the core instance
    ai360.add_bot(ai360_bot)

    # Optional: show all bots
    print("\nAll bots initialized. Connected bots:")
    for bot in ai360.bots:
        print("-", bot.__class__.__name__)

    # Simple test messages
    messages = ["Hello AI-360!", "How are you?", "What time is it?", "Testing one two three."]
    for msg in messages:
        print("\nYou:", msg)
        print("AI360Bot:", ai360_bot.respond(msg))
        print("HelperBot:", helper_bot.greet())  # or receive method if you prefer
        ai360.store_memory("chat_history", [{"user": msg, "ai360": ai360_bot.respond(msg)}])

if __name__ == "__main__":
    main()
