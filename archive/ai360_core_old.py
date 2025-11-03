import json
import os

# Load memory if it exists
MEMORY_FILE = "ai360_memory.json"
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
else:
    memory = {}

def get_user_memory(user_id):
    if user_id not in memory:
        memory[user_id] = {}
    return memory[user_id]

def core_response(user_input, user_id="default_user"):
    user_mem = get_user_memory(user_id)
    user_mem["last_input"] = user_input
    return f"AI-360 ({user_id}) received: {user_input}"

def save_memory():
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def main():
    print("AI-360 Core running. Type 'exit' to quit.")
    user_id = input("Enter your user ID: ").strip()
    if not user_id:
        user_id = "default_user"

    while True:
        user_input = input(f"{user_id} >> ")
        if user_input.lower() == "exit":
            break
        response = core_response(user_input, user_id)
        print(response)
        save_memory()

if __name__ == "__main__":
    main()
