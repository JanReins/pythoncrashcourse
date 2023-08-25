import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))
print('Phone number found: ' + mo.group())
print('Phone number found: ' + mo.group(0))

<<<<<<< HEAD
print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))
=======
>>>>>>> 8d84cbf86d8a03fde62be3161c58e8d60e10ce70
