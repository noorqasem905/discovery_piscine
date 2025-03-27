#!/usr/bin/python3

try:
enter = input("What you gotta say? : ")
    while 1:
        if enter == "STOP":
            break
        enter = input("I got that! Anything else? : ")
except:
    print("invalid input")
