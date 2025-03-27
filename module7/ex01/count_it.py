#!/usr/bin/env python3
import sys
try:
    if len(sys.argv) != 1:
        print("parameters: " + str(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print(str(sys.argv[i]) + ": " + str(len(sys.argv[i])))
    else:
        print("none")
except:
    print("Invalied Argments", file= sys.stderr)