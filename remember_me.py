from pathlib import Path
import json

username = input("What's your name? ")\

usernames = Path('username.json')
names = json.dumps(username)
usernames.write_text(names)