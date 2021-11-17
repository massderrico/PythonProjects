"""Author: Massimo D'Errico"""

class Car: #class 1
    def __init__(self, make, year, color): # 3 attributes
        self.make = make
        self.year = year
        self.color = color
    def made(self):
        print(f"my {self.make} is made in {self.year}.")
    def car_color(self):
        print(f"My {self.make} is painted {self.color}.")

my_car = Car('Honda', 2005, 'black')       # object 1
my_other_car = Car('Ferrari', 2019, 'red') # object 2

my_car.made() #calling methods
my_other_car.car_color()

class House: #class 2
    def __int__(self,roof, sqft,floors): # 3 attributes
        self.roof = roof
        self.sqft = sqft
        self.floors = floors
    def interior(self):
        print(f"This house has {self.floors} and is {self.sqft} square feet")
    def exterior(self):
        print(f"The roof of this house is {self.roof}")

left_neighbor = House('brown', 1000, 2) #object 1
right_neighbor = House('grey', 3500, 3) #object 2

left_neighbor.exterior() # calling methods
right_neighbor.interior()