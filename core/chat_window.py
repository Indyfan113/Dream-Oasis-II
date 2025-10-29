
# core/chat_window.py

from bots.helper_bot import HelperBot
from bots.ai360_bot import AI360Bot

def main():
    helper_bot = HelperBot()
    ai360_bot = AI360Bot()

    print("AI360Bot is ready.")
    print("Bot 'HelperBot' is ready. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting chat. Goodbye!")
            break

        response_ai360 = ai360_bot.respond(user_input)
        response_helper = helper_bot.receive(user_input)  # or helper_bot.greet() if preferred

        print(f"AI360Bot: {response_ai360}")
        print(f"HelperBot: {response_helper}")

if __name__ == "__main__":
    main()
