import json
import os

# File for saving memory
MEMORY_FILE = "ai360_memory.json"

# Load memory if it exists
if os.path.exists(MEMORY_FILE):
    try:
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)
    except json.JSONDecodeError:
        print("Warning: memory file corrupted. Starting fresh.")
        memory = {}
else:
    memory = {}

# Define token types
TOKEN_TYPES = ["iron", "gold", "diamond", "seed", "soil", "ice"]

# --- Memory management ---
def get_user_memory(user_id):
    if user_id not in memory:
        memory[user_id] = {
            "tokens": [],
            "last_input": ""
        }
    return memory[user_id]

def save_memory():
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

# --- Token commands ---
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

# --- Core response ---
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

    # Normal responses with token effects
    user_mem["last_input"] = user_input
    save_memory()

    if "ice" in user_mem["tokens"]:
        return f"❄️ AI-360 ({user_id}) [ice active]: {user_input}"
    else:
        return f"AI-360 ({user_id}): {user_input}"

# --- Main session loop ---
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
