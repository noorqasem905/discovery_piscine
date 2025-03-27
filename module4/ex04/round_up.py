#!/usr/bin/python3
try:
enter = input("Give me a number: ")
    enter = float(enter)
    if enter != int(enter) and enter > 0:
        enter = int(enter) + 1
    else:
        enter = int(enter)
    print(enter)
except ValueError:
    print("This is not a number.")