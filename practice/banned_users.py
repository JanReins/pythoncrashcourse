banned_users = ['andrew', 'carolina', 'david']
user = input("username: ")

if user not in banned_users:
    print(f"{user.title()}, successfull entry")
else:
    print(f"{user.title()}, you are banned!")

