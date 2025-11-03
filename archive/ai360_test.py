import json

memory = {}

def core_response(user_input, user_id="default_user"):
    return f"{user_id} received: {user_input}"

def main():
    print("Test running. Type 'exit'")
    user_id = input("Enter user ID: ")
    while True:
        s = input(f"{user_id} >> ")
        if s.lower() == "exit":
            break
        print(core_response(s, user_id))

if __name__ == "__main__":
    main()
