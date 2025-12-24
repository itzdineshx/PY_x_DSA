#This Program calculates the area of a circle given its radius
# radius = pi*r²
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * math.pow(radius, 2)
print("The area of the Circle is {:.2f}".format(area))