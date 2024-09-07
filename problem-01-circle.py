# Problem 01: Find area and perimeter of a circle

import math

# Circle - input radius
radius = float(input("Enter the radius of the circle: "))

# Calculate area and perimeter
circle_area = math.pi * radius ** 2
circle_perimeter = 2 * math.pi * radius

print("Circle Area: {}".format(circle_area))
print("Circle Perimeter: {}".format(circle_perimeter))