sandwich_orders = ["hamburger", "cheeseburger","pastrami", "hotdog", "club sandwich", "BLT",
                 "peanut butter and jelly", "grilled cheese","pastrami", "chicken salad sandwich",
                 "tuna salad sandwich", "egg salad sandwich", "pastrami",]
finished_sandwiches = []

print("The Deli has run out of pastrami\n")

for pastrami in sandwich_orders:
    sandwich_orders.remove("pastrami")

for sandwich in sandwich_orders:
    print(f"I made you a {sandwich} bb")
    sandwich_orders.remove(sandwich)
    finished_sandwiches.append(sandwich)

print("\nThese are all the sandwich made: \n")

for sandwich in finished_sandwiches:
    print(sandwich)