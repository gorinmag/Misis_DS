import json
with open("task_4.json", "r", encoding="utf-8") as f:
    ts4 = json.load(f)
print(f"https://t.me/{ts4['from_user']['username']}")