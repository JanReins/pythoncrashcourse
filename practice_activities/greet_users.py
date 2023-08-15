def bday_greeting(names):
    for name in names:
        message = f"Happy Birthday {name.title()}!"
        print(message)
usernames = ['hannah', 'ty', 'margot']
bday_greeting(usernames)