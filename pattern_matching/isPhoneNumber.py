import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phone_number = 'My number is 415-555-4242.'
mo = phoneNumRegex.search(phone_number)
print(mo.group(1))
print(mo.group(2))
print(mo.group())
print(mo.group(0))
print(mo.groups())