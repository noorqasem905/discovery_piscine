#!/usr/bin/python3
def  greetings(st = "Error! It was not a name."):
    if (not isinstance(st, str)):
        print("Hello, " + st)
    else:
        print(st)
try:
    greetings()
    greetings("NOOR Aldeen")
    greetings("batata")
    greetings("batata")
except:
    print("ERROR")