import math

radius = eval(input("Enter the radius: "))
area = radius * radius * math.pi
# compute area
if area < 0:
    print("input incorrect")
else:
    print("The area for the circle of radius", radius, "is", area)
