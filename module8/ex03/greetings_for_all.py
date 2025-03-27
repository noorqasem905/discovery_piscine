#!/usr/bin/python3
def  greetings(st = "Error! It was not a name."):
    if type(st) == int:
        print("Error! It was not a name.")
    elif (isinstance(st, str) and st != "Error! It was not a name."):
        print("Hello, " + st)
    else:
        print("Hello, noble stranger.")
try:
    greetings()
    greetings("NOOR Aldeen")
    greetings("batata")
    greetings(77)
except:
    print("ERROR")