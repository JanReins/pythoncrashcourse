from pathlib import Path
import json

path = Path('username.json')
if path.exists():
    names = path.read_text()
    username = json.loads(names)
else:
        print(f"We'll remember you when you come back!")

print(f"Welcome back, {username}!")
