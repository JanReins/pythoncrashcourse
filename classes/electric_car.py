class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("Fill gas")


class Battery:
    def __init__(self, battery_size=40):
        self.batter_size = battery_size

    def describe_battery(self):
        print((f"This car has a {self.batter_size} -kWh battery>"))
    
    def get_range(self):
        range = int(self.batter_size)*3.75
        print(f"This car can go about {range} miles on a full charge")

class Electric_Car(Car):

    def __init__(self, make, model, year): 
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't have gas tank")

my_leaf = Electric_Car('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.fill_gas_tank()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
