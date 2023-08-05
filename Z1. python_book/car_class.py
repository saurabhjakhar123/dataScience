class Car:
    """A Simple car class => model, year, company"""

    def __init__(self, model, year, company):
        self.model = model
        self.year = year
        self.company = company

        # create a default attribute 
        self.distance_covered = 0

    def describe_car(self):
        describe = f"{self.model} {self.year} {self.company}"
        print(describe)
    
    def distance_cover(self):
        print(f"This car coverd a distance of {self.distance_covered} km.")

    # CHANGE THE VALUE OF A ATTRIBUTE THROUGH A METHOD
    def update_distance_covered(self, new_distance):
        self.distance_covered = new_distance

car_1 = Car("Dezire", 2014, "Maruti Suzuki")
car_1.distance_cover()
car_1.describe_car()

# first approch to change the attribute value by instance
car_1.distance_covered = 25
car_1.distance_cover()

car_1.update_distance_covered(50)
car_1.distance_cover()

# make a inherit class from car
class ElectricCar(Car):
    def __init__(self, model, year , company):
        super().__init__(model, year, company)
        


my_ev = ElectricCar("Model S",2019, "Tesla")
my_ev.describe_car()