#!/usr/bin/env python3
import sys
try:
    if len(sys.argv) == 2:
        enter = str(input("What was the parameter? "))
        if (enter) == (sys.argv[1]):
            print("Good job!")
        else:
            print("Nope, sorry...")
    else:
        print("none")
except:
    print("Invalied Argments", file= sys.stderr)