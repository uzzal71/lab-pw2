# Find status of an integer (zero, +ve, -ve)

# Input integer
num = int(input("Enter an integer: "))

# Check the status of the integer
if num > 0:
    print("{} is Positive".format(num))
elif num < 0:
    print("{} is Negative".format(num))
else:
    print("The number is Zero")