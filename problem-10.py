# 10. How to take input from the user & print output

# Taking multiple inputs from the user
name = raw_input("Enter your name: ")
# name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))

# Printing output
print("Hello {}, you are {} years old and {} meters tall.".format(name, age, height))