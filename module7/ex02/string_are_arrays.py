#!/usr/bin/env python3
import sys
try:
    i = 0
    counter = 0
    if len(sys.argv) == 2:
        st = sys.argv[1]
        while i < len(st):
            if (st[i]) == "z":
                counter += 1
            i += 1
        if counter == 0:
            print("none")
        else:
            while counter != 0:
                print('z', end="")
                counter -= 1
    else:
        print("none")
except:
    print("Invalied Argments", file= sys.stderr)