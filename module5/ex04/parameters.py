#!/usr/bin/env python3
import sys
try:
    print("Number of parameters: " + str(len(sys.argv) - 1) + ".")
except:
    print("ERROR", file=sys.stderr)