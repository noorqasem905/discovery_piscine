#!/usr/bin/env python3
import sys
try:
    if len(sys.argv) == int(2):
        st = str(sys.argv[1])
        print(st.upper())
    else:
        print("none")
except ImportError:
    print("ERROR", file=sys.stderr)