# 7-8. Apply function to solve problems 1-6 (any 2)

def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

# Input
num = int(input("Enter an integer: "))

# Function call
status = check_even_odd(num)
print("The number {} is {}".format(num, status))