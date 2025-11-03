# run_full_ai360_test.py
from ai_360.ai360_core import AI360
from bots.helper_bot import HelperBot
from bots.ai360_bot import AI360Bot

def main():
    # Initialize the AI-360 core logic
    ai360 = AI360()
    ai360.initialize()

    # Initialize and add HelperBot
    helper_bot = HelperBot()
    ai360.add_bot(helper_bot)

    # Initialize and add AI360Bot
    ai360_bot = AI360Bot(ai360)  # pass the AI360 core
    ai360.add_bot(ai360_bot)

    print("\nAll bots initialized. Connected bots:")
    for bot in ai360.bots:
        print("-", bot.__class__.__name__)

    # Test messages through both bots
    test_messages = [
        "Hello AI-360!",
        "How are you?",
        "What time is it?",
        "Testing one two three."
    ]

    for msg in test_messages:
        print(f"\nYou: {msg}")
        # AI360Bot responds
        response_ai360 = ai360_bot.respond(msg)
        print(f"AI360Bot: {response_ai360}")
        # HelperBot responds
        response_helper = helper_bot.greet() if msg.lower().startswith("hello") else helper_bot.receive(msg)
        print(f"HelperBot: {response_helper}")

        # Store conversation in AI360 memory
        chat_history = ai360.recall_memory("chat_history") or []
        chat_history.append({"user": msg, "ai360": response_ai360})
        ai360.store_memory("chat_history", chat_history)

    print("\nFinal chat history stored in AI360 memory:")
    print(ai360.recall_memory("chat_history"))

if __name__ == "__main__":
    main()
