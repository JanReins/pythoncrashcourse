from pathlib import Path

contents = "I love programming. \n"
contents += "I love creating new games. \n"
contents += "I also love working with data. \n"

path = Path('Programming.txt')
path.write_text("I love programming")
