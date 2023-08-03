#toppings = ['mushrooms', 'green peppers', 'extra cheese']

#requested_topping = input("enter your pizza topping of choice: ")

#if requested_topping in toppings:
#    print(f"Adding your {requested_topping}.")
#else:
#    print(f"Sorry, we don't have {topping}.")
#print("\nFinished making your pizza")


#using multiple lists
available_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'olives', 'peperoni', 'pineapple']
requested_toppings = ['french fries', 'mushrooms', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"sorry we don't have {requested_topping}.")

print("\nFinished making your pizza.")


