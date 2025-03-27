#!/usr/bin/env python3
import sys
try:
    if len(sys.argv) > int(1):
        print(str(sys.argv[1]))
    else:
        print("none")
except:
    print("ERROR",  file=sys.stderr)