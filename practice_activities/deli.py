sandwich_orders = ["hamburger", "cheeseburger", "hotdog", "club sandwich", "BLT",
                 "peanut butter and jelly", "grilled cheese", "chicken salad sandwich",
                 "tuna salad sandwich", "egg salad sandwich"]
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made you a {sandwich} bb")
    sandwich_orders.remove(sandwich)
    finished_sandwiches.append(sandwich)

