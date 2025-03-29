import os
import json

MEMORY_DIR = "memory_store"
os.makedirs(MEMORY_DIR, exist_ok=True)

def get_memory(user_id):
    path = os.path.join(MEMORY_DIR, f"{user_id}.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return "\n".join([f"User: {q}\nMoBi: {a}" for q, a in data[-3:]])
    return ""

def update_memory(user_id, question, answer):
    path = os.path.join(MEMORY_DIR, f"{user_id}.json")
    data = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    data.append((question, answer))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data[-10:], f, ensure_ascii=False, indent=2)
