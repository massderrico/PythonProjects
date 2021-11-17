side1 = int(input("what is the first side of the triangle: "))  #defines the side of the trignle
side2 = int(input("what is the second side of the triangle: "))
side3= int(input("what is the third side of the triangle: "))

if side1 == side2 == side3: #checks if all the sides are equal (equilateral)
    print("this is an equilateral tringle")
elif side1 != side2 != side3:
    print("this is triangle is scalene") #checks to see if none of the side are equal (scalene)
else:
    print("this triangle is isosceles") #any triangle beside equilateral and scalene are isosceles
