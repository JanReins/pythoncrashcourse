from pathlib import Path
import json


number = input("What's your favorit number? ")

path = Path('fave_number.json')
numbers = json.dumps({'number': number})
path.write_text(numbers)