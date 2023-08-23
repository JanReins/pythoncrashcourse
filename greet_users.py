from pathlib import Path
import json

path = Path('username.json')
if path.exists():
    names = path.read_text()
    username = json.loads(names)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    names = json.dumps(username)
    path.write_text(names)
    print(f"We'll remember you when you come back, {username}!")
