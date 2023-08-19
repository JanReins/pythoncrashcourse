from car import Car

class Electric_Car(Car):

    def __init__(self, make, model, year): 
        super().__init__(make, model, year)

my_leaf = Electric_Car('nisan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())