current_users = ['Airah', 'James', 'Darrel', 'Marilyn', 'Marcelino', 'Admin']
new_users = ['Pete', 'Rocket', 'Gamorra', 'Groot', 'Bluegirl', 'Mantis', 'Darrel']

#new_user = input("Enter username: ").title()

for user in new_users:
    if user in current_users:
        print("Sorry username in use, enter another username")
    else:
        print(f"Username {user} available.")

