#!/usr/bin/env python3
import sys
i = 0
try:
    size = (len(sys.argv))
    if size > int(2):
        while i < size:
            print(sys.argv[size - 1])
            size = size - 1
    else:
        print("none")
except: 
    print("ERROR",  file=sys.stderr)