from pathlib import Path
import json


number = input("What's your favorit number? ")

path = Path(3)
numbers = json.dumps({'number': number})
path.write_text(numbers)