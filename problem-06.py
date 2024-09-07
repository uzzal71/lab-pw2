# Find the factorial value of a positive integer

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input a positive integer
num = int(input("Enter a positive integer to find its factorial: "))

# Output factorial
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("The factorial of {} is {}".format(num, factorial(num)))
