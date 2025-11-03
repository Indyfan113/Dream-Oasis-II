import json
import os

# Load memory if it exists
MEMORY_FILE = "ai360_memory.json"
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
else:
    memory = {}

# Token types
TOKEN_TYPES = ["iron", "gold", "diamond", "seed", "soil", "ice"]

def get_user_memory(user_id):
    if user_id not in memory:
        memory[user_id] = {
            "tokens": [],
            "last_input": ""
        }
    return memory[user_id]

def add_token(user_id, token):
    if token in TOKEN_TYPES:
        user_mem = get_user_memory(user_id)
        if token not in user_mem["tokens"]:
            user_mem["tokens"].append(token)
            save_memory()
            return f"Token '{token}' added to {user_id}."
        else:
            return f"{user_id} already has token '{token}'."
    else:
        return f"Invalid token type: '{token}'."

def remove_token(user_id, token):
    user_mem = get_user_memory(user_id)
    if token in user_mem["tokens"]:
        user_mem["tokens"].remove(token)
        save_memory()
        return f"Token '{token}' removed from {user_id}."
    else:
        return f"{user_id} does not have token '{token}'."

def save_memory():
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def core_response(user_input, user_id="default_user"):
    user_mem = get_user_memory(user_id)

    # Command handling
    if user_input.startswith("/add_token "):
        token = user_input[len("/add_token "):].strip()
        return add_token(user_id, token)
    
    if user_input.startswith("/remove_token "):
        token = user_input[len("/remove_token "):].strip()
        return remove_token(user_id, token)
    
    if user_input.startswith("/list_tokens"):
        return f"{user_id} has tokens: {user_mem['tokens']}"

    # Regular response with optional token effect
    user_mem["last_input"] = user_input
    if "ice" in user_mem["tokens"]:
        return f"❄️ AI-360 ({user_id}) [ice active]: {user_input}"
    else:
        return f"AI-360 ({user_id}): {user_input}"

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

if __name__ == "__main__":
    main()
