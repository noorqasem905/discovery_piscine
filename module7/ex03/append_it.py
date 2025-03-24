#!/usr/bin/python3
import sys
try:
        i = 0
        size = len(sys.argv)
        if size != 1:
            for x in (sys.argv[1:]):
                i = x.rfind("ism")
                if i == -1 or len(x) - 3 > i:
                    print(x.strip() + "ism")
                else:
                    print(x.strip())
        else:
            print("none")

except:
    print("invalid input")