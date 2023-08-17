class Restaurant:
    def __init__(self, restaurant_name, cuisin_type):
        self.restuarant_name = restaurant_name
        self.cuisin_type = cuisin_type
    

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} is a {cuisin_type} 5 star restuarant")

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open from 1pm to 12 am')

    
cebu_restaurant = Restaurant("Rico's Lechon", "Roasted suckling pig")
cebu_restaurant.describe_restaurant()
cebu_restaurant.open_restaurant()
