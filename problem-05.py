# Print multiplication table for an integer

# Input integer
num = int(input("Enter an integer to print its multiplication table: "))

# Print multiplication table
for i in range(1, 11):
    print("{} x {} = {}".format(num, i, num * i))