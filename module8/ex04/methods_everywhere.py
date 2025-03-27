#!/usr/bin/python3
import sys

def shrink(st):
    x = slice(8)
    print(st[x])

def enlarge(st):
    i = 0
    x = slice(len(st))
    print(st[x], end = "")
    i = 8 - len(st)
    while(i > 0):
        print('Z', end = "")
        i -= 1
    print()
try:
    i = 1
    while i < len(sys.argv):
        if len(sys.argv[i]) > 8:
            shrink(sys.argv[i])
        elif len(sys.argv[i]) < 8:
            enlarge(sys.argv[i])
        else:
            print(sys.argv[i])
        i += 1
except Exception as e:
    print(f"ERROR: {e}")
