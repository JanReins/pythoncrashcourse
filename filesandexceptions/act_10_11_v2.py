from pathlib import Path
import json

path = Path('fave_number.json')
content = path.read_text()
numbers = json.loads(content)
print(f"I know your favorite number! it'{numbers['number']}")