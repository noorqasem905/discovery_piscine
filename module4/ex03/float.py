#!/usr/bin/python3
enter = (input("Give me a number: "))
enter = float(enter)

if enter != int(enter):
    print("This number is a decimal.")
else:
    print("This number is an integer.")