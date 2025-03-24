#!/usr/bin/python3
enter = input("Enter a number\n")
i = 0
i = int(i)
try:
    enter = int(enter)
    while i <= 9:
        result = int(i * enter)
        print(str(i) + " x " + str(enter) + " = ", result)
        i = i + 1
except:
    print("invalid input")