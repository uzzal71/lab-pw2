# Even odd status of an integer

# Input integer
num = int(input("Enter an integer: "))

# Check if even or odd
if num % 2 == 0:
    print("{} is Even".format(num))
else:
    print("{} is Odd".format(num))