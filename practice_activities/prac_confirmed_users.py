unconfirmed_users = ['alice', 'brian', 'candace']
#Looping thru dictionaries

confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying users: {current_user}")

    confirmed_users.append(current_user)
print("\nThe following users have been confirmed: ")

for user in confirmed_users:
    print(user.title())
