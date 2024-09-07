# 7-8. Apply function to solve problems 1-6 (any 2)

import math

def circle_properties(radius):
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter

# Input
radius = float(input("Enter the radius of the circle: "))

# Function call
area, perimeter = circle_properties(radius)
print("Area: {}, Perimeter: {}".format(area, perimeter))