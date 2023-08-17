class User:
    def __init__(self, first_name, last_name, age=0, gender=""):
        self.firstname = first_name
        self.lastname = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(self.firstname, self.lastname, self.age, self.gender)

        
    def greet_user(self):
        print(f"Greetings {self.firstname}, son of {self.lastname}, {self.gender} and {self.age} years of age")

user1 = User('Jan', 'Rein', 24, 'Male')
user2 = User('Airah', 'Meneses', 25, 'Female')
user3 = User('Draig', 'Rein', 30)

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
