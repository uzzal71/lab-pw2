# 9. Casting problem: check whether an integer is fraction or not

# Input a number
num = float(input("Enter a number: "))

# Check if the number has a fractional part
if num == int(num):
    print("{} is an integer.".format(num))
else:
    print("{} is a fraction.".format(num))