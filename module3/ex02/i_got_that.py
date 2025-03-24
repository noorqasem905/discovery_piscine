#!/usr/bin/python3
enter = input("What you gotta say? : ")
try:
    while 1:
        if enter == "STOP":
            break
        enter = input("I got that! Anything else? : ")
except:
    print("invalid input")