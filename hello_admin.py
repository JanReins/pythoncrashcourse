username_database = ['Airah', 'James', 'Darrel', 'Marilyn', 'Marcelino', 'Admin']

#username = input("Enter user name: ").title()

for username in username_database:
    if username == 'Admin':
        print("Welcome admin, would you like to log in?")
    elif username in username_database:
        print(f"Hello {username}.")
    else:
        print("We need to find some users")
