#!/usr/bin/python3
enter = input("Enter a number less than 25\n")
enter = int(enter)
try:
    if enter > 25:
        print("Error")
    else:
        while enter <= 25:
            print("Inside the loop, my variable is " + str(enter))
            enter = enter + 1
except:
    print("invalid input")