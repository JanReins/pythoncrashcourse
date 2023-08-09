while True:
    age = int(input('enter age: '))
    ticket_cost = 0
    if age < 3:
        ticket_cost = 0
        print(f"Your ticket costs is {ticket_cost}.")
    elif age < 12:
        ticket_cost = 10
        print(f"Your ticket costs is {ticket_cost}.")
    elif age > 12:
        ticket_cost = 15
        print(f"Your ticket costs is {ticket_cost}.")
    else:
        continue