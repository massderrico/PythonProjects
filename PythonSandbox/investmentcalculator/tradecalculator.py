class Ice_Cream:
       def __init__(self,color, flavour):
              self.color = color
              self.flavour = flavour
       def lick(self):
              print(f"this {self.flavour} is {self.color}")

first_ice = Ice_Cream("red","strawberry")

dict1 = { "key1": 1,
          "key2": 2}

dict2 = { "key1": 1,
          "key2": 3}
"""
def dict_intersect(dict1, dict2):
       for x,y in dict1.items():
              return(x,y)
       for w,z in dict2.items():
              return (w,z)
       for (x,y) in (w,z):
              print(x,y)
              """

def dict_intersect(dict1, dict2):
       for dict1 in  dict2:
              print(dict1)




dict_intersect(dict1,dict2)



""""
class Country:
       def __init__(self, name, population, area):
              self.name = name
              self.population = population
              self.area= area
       def is_larger(self, other_country):
              if self.area > other_country.area :
                     print(True)
              else:
                     print(False)
       def population_density(self):
              print(str(self.population/self.area))





canada = Country("Canada", 37590000, 9984670)

ecuador = Country("Ecuador", 17300000, 283561)

canada.is_larger(ecuador)  # Output should be False

canada.population_density()


dict_color = { "R":0.5,
          "G": 0.4,
          "B": 0.1
          }

def is_balanced(dict_color):
       check = dict_color["R"]+ dict_color["G"]+ dict_color["B"]
       if check == 1.0:
              print(True)
       else:
              print(False)

is_balanced(dict_color)


n=7
for i in range(n):
    print(' ' * i + 'T' * (2*n - (2*i+1)) )

"""