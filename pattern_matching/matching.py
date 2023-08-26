import re

heroRegex = re.compile(r'Batman|Tina Fey')
title_name = "Batman and Tina Fey"
mo1 = heroRegex.search(title_name)
print(mo1.group(2))
