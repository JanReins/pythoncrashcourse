sandwich_orders = ["hamburger", "cheeseburger","pastrami", "hotdog", "club sandwich", "BLT",
                 "peanut butter and jelly", "grilled cheese","pastrami", "chicken salad sandwich",
                 "tuna salad sandwich", "egg salad sandwich", "pastrami",]
finished_sandwiches = []

print("The Deli has run out of pastrami\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made you a {sandwich} bb")
    finished_sandwiches.append(sandwich)

print("\nThese are all the sandwich made: \n")

for sandwich in finished_sandwiches:
    print(sandwich)