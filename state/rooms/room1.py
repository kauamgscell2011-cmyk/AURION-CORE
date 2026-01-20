# Sala 1 – Criação do Projeto
# rooms/room1.py

def run_room1(state):
    print("🎬 SALA 1 — CRIAÇÃO DO PROJETO\n")

    if state["project"] is None:
        name = input("Nome do projeto (série ou filme): ")
        state["project"] = {
            "name": name,
            "episodes": [],
            "films": []
        }
        print(f"✅ Projeto '{name}' criado.")
    else:
        print(f"🔁 Retomando projeto '{state['project']['name']}'")

    print("\n➡️ Indo para a Sala 2...")
    state["current_room"] = 2
