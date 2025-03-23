#!/usr/bin/python3
num_1 = input("Enter the first number:\n")
num_2 = input("Enter the second number:\n")
num_1 = int(num_1)
num_2 = int(num_2)
result = num_1 * num_2
print(str(num_1) + " x " + str(num_2) + " = " + str(result))
if result > 0:
    print("The result is positive.\n")
elif result < 0:
    print("The result is negative.\n")
else:
    print("The result is zero.\n")