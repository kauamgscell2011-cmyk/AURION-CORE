# aurion.py
import json
import os

STATE_PATH = "state/progress.json"

def load_state():
    if not os.path.exists("state"):
        os.makedirs("state")
    if not os.path.exists(STATE_PATH):
        return {
            "current_room": 1,
            "project": None
        }
    with open(STATE_PATH, "r") as f:
        return json.load(f)

def save_state(state):
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=4)

def start_room(room_number, state):
    if room_number == 1:
        from rooms.room1 import run_room1
        run_room1(state)
    elif room_number == 2:
        from rooms.room2 import run_room2
        run_room2(state)
    elif room_number == 3:
        from rooms.room3 import run_room3
        run_room3(state)
    else:
        print("🚫 Sala inexistente.")

def main():
    print("\n=== AURION :: HUB CENTRAL ===\n")
    state = load_state()

    print(f"📂 Projeto atual: {state['project']}")
    print(f"🚪 Sala atual: {state['current_room']}\n")

    start_room(state["current_room"], state)
    save_state(state)

if __name__ == "__main__":
    main()
