#!/usr/bin/python3
try:
enter = input("Enter a number less than 25\n")
    enter = int(enter)

    if enter > 25:
        print("Error")
    else:
        while enter <= 25:
            print("Inside the loop, my variable is " + str(enter))
            enter = enter + 1
except:
    print("invalid input")