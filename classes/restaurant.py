class Restaurant:
    def __init__(self, restaurant_name, cuisin_type):
        self.restaurant_name = restaurant_name
        self.cuisin_type = cuisin_type
    

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} is a {self.cuisin_type} cuisin 5 star restuarant")

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open from 1pm to 12 am')

    
cebu_restaurant_1 = Restaurant("Rico's Lechon", "Roasted suckling pig")
cebu_restaurant_2 = Restaurant("La Marea", "Seafood dishes")
cebu_restaurant_3 = Restaurant("Lantaw Native Floating Restaurant", "Filipino dishes")

cebu_restaurant_1.describe_restaurant()
cebu_restaurant_2.describe_restaurant()
cebu_restaurant_3.describe_restaurant()
#cebu_restaurant.open_restaurant()
