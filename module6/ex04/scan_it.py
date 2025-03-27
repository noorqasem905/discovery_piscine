#!/usr/bin/env python3
import sys
try:
    if len(sys.argv) == 3:
        i = 0
        counter = 0
        first = sys.argv[1]
        arr = sys.argv[2].split()
        while len(arr) > i:
            if arr[i] == first:
                counter = counter + 1
            i = i + 1
        if counter == 0:
            print("none")
        else:
            print(str(counter))
    else:
        print("none")
except: 
    print("ERROR",  file=sys.stderr)