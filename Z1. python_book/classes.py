# Cretaing a class for a Dog

class Dog:
    """Class for a Dog"""
    
    def __init__(self, name, age):
        """Initialize name and age of a dog """
        self.name = name
        self.age = age
    
    def sit(self):
        """Give command to sit"""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Giving command to roll over"""
        print(f"{self.name} is rollinf over.")



# calling a class

def fun_1():
    myDog = Dog("Shera", 5)
    print(f"My dog name is {myDog.name}.")
    print(f"My dog age is {myDog.age} years old.")
    myDog.sit()


def fun_2():
    yourDog = Dog("Tommy", 3)
    print(f"Your dog name is {yourDog.name}.")
    print(f"Your dog age is {yourDog.age} years old.")
    yourDog.sit()


fun_list = [fun_1, fun_2]
for i in fun_list:
    i()


# 9.1 : Restaurant
class Restaurant:
    """Classes name Restaurant"""

    def __init__(self, restaurant_name, *cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant name : {self.restaurant_name}.")
        print(f"Cuisine Type : {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is open.")
    

restaurant_1 = Restaurant("Taj Hotel", "Indiane", "chinese")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
#-----

restaurant_2 = Restaurant("farmidev", "Indiane")
restaurant_2.describe_restaurant()

#-----

restaurant_3 = Restaurant("Oberoi","Indiane", "Chinese", "Japanese", "Korean")
restaurant_3.describe_restaurant()


# 9.3 Users:

class Users:
    def __init__(self, fname, lname, age):
        self.first_name = fname
        self.last_name = lname
        self.age = age
    
    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} years old.")
    
    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!")

user_1 = Users("saurabh", "jakhar", 26)
user_1.describe_user()
user_1.greet_user()

# 9.4 : Number served
class Restaurant:
    """Classes name Restaurant"""

    def __init__(self, restaurant_name, *cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Restaurant name : {self.restaurant_name}.")
        print(f"Cuisine Type : {self.cuisine_type}.")
        print(f"Number served today : {self.number_served}")
    
    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is open.")
    
    def set_number_served (self, number):
        self.number_served = number

    def increement_number_served(self, no_served):
        self.number_served += no_served

restaurant = Restaurant("HotelTaj", "Indian")
restaurant.set_number_served(5)
restaurant.describe_restaurant()

restaurant.increement_number_served(10)
restaurant.describe_restaurant()

# 9.5 : Login attempts

class Users:
    def __init__(self, fname, lname, age):
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} years old.")
    
    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!")

    def increement_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user_1 = Users("saurabh", "jakhar", 26)

user_1.increement_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)