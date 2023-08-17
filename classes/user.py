class User:
    def __init__(self, first_name, last_name, age=0, gender=""):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name, self.last_name, self.age, self.gender)

        
    def greet_user(self):
        print(f"Greetings {self.first_name}, son of {self.last_name}, {self.gender} and {self.age} years of age.")
        print("Welcome to the accendants! \n")

    def increment_login_attempts(self, attempts=1):
        self.login_attempts += attempts
        print(f"login attemp number {self.login_attempts}\n")

    def reset_login_attempts(self, reset_login=0):
        if self.login_attempts > 3:
            self.login_attempts = 0
            print("Login attempts reset.\n")
        else:
            print("No need to reset login attempts.\n")


user1 = User('Jan', 'Rein', 24, 'Male')
user2 = User('Airah', 'Meneses', 25, 'Female')

user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()

user2.describe_user()
user2.greet_user()
user2.increment_login_attempts()

user1.increment_login_attempts()
user2.increment_login_attempts()

user1.increment_login_attempts()
user2.increment_login_attempts()

user1.increment_login_attempts()
user2.increment_login_attempts()

user1.reset_login_attempts()
user2.reset_login_attempts()

user1.increment_login_attempts()
user2.increment_login_attempts()
