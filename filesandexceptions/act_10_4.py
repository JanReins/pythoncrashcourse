from pathlib import Path
import json

name = input("Please enter your name: ")
guest_list = Path("guest.json")

guest_data = {"name": name}

guest_json = json.dumps(guest_data)
guest_list.write_text(guest_json)