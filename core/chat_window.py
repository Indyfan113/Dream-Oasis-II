
# core/chat_window.py

from ai_360.ai360_core import AI360
from bots.helper_bot import HelperBot
from bots.ai360_bot import AI360Bot

def main():
    # Initialize core
    ai360 = AI360()
    ai360.initialize()

    # Initialize bots
    helper_bot = HelperBot()
    ai360.add_bot(helper_bot)

    ai360_bot = AI360Bot(ai360)
    ai360.add_bot(ai360_bot)

    print("AI360Bot is ready.")
    print("Bot 'HelperBot' is ready. Type 'exit' to quit, 'history' to view chat history.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Exiting chat. Goodbye!")
            break
        elif user_input.lower() == "history":
            history = ai360_bot.show_history()
            if not history:
                print("No chat history yet.")
            else:
                print("Chat history:")
                for entry in history:
                    print(f"User: {entry['user']} | AI360: {entry['ai360']}")
            continue

        # Responses
        response_ai360 = ai360_bot.respond(user_input)
        response_helper = helper_bot.receive(user_input)

        print(f"AI360Bot: {response_ai360}")
        print(f"HelperBot: {response_helper}")

if __name__ == "__main__":
    main()
