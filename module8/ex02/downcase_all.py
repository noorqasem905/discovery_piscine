#!/usr/bin/python3
import sys
def  downcase_it(st):
    return (st.lower())
try:
    if len(sys.argv) == (1):
        print("none")
    else:
        for i in range(1, len(sys.argv)):
            print(downcase_it(sys.argv[i]))
except:
    print("ERROR", file=sys.stderr)