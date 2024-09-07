# Problem 01: Find area and perimeter of a rectangle

# Rectangle - input width and height
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

# Calculate area and perimeter
rectangle_area = width * height
rectangle_perimeter = 2 * (width + height)

print("Rectangle Area: {}".format(rectangle_area))
print("Rectangle Perimeter: {}".format(rectangle_perimeter))