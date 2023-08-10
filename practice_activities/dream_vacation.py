dream_vacations = {}

while True:
    name = input("Hi can I ask your name? enter 'quit' or 'exit' to stop ")
    if name == 'quit' or name  == 'exit':
        break
    dream_vacation = input(f"Hi {name}, if you could visit one place in the world, where would you go? ")
    dream_vacations[name] = dream_vacation

print("Dream vacation results ")
for name, dream_vacation in dream_vacations.items():
    print(f"{name} would like to visit {dream_vacation}")

