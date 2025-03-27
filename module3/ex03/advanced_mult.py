#!/usr/bin/env python3

i = 0
j = 0
result = 0
try:
    while i <= 10:
        result = i
        print("Table of " + str(i) + ": ", end="")
        while j <= 10:
            result = j * i
            print(result, end=" ")
            j += 1
        print()
        i += 1
        j = 0
except: 
    print("invalied input", file=sys.stderr)
