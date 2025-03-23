#!/usr/bin/python3
import sys
i = 0
i = int(i)
size = int(len(sys.argv))
if size > int(1):
    while i < size:
        print(sys.argv[i])
        i = i + 1
else:
    print("none")