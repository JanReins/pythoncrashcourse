class Restaurant:
    def __init__(self, restaurant_name, cuisine_type,):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} is a {self.cuisine_type} cuisin 5 star restuarant")

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open from 1pm to 12 am')

    def set_number_served(self, customer_served):
        self.number_served = customer_served
        print(f"{self.number_served} customers was served")

    def increment_number_served(self, customers):
        self.number_served += customers
        print(f"{self.number_served} customers was served")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'cookies and cream', 'avocado']

    def show_flavors(self):
        print(f"Available Ice Cream flavors: ")
        for flavor in self.flavors:
            print(flavor)

ice_cream_stand = IceCreamStand("Sweet Delights", "Ice Cream")
ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.show_flavors()