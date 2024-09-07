# Find the diagonal of a square by using given a side value

import math

# Input side length of square
side = float(input("Enter the side length of the square: "))

# Calculate diagonal using the Pythagorean theorem
diagonal = math.sqrt(2) * side

print("The diagonal of the square is: {}".format(diagonal))