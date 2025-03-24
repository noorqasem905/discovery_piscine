#!/usr/bin/python3
import sys
try:
        i = 0
        size = len(sys.argv)
        if size == 3:
            size = abs(int(sys.argv[2]) - int(sys.argv[1]))
            if size > 0:
                arr = [None] * (abs(size) + 1)
                if size > 0:
                    for i in range(size + 1):
                        arr[i] = i + int(sys.argv[1])
                else:
                    for i in range(size + 1):
                        arr[i] = i - int(abs(sys.argv[2]))
            else:
                arr = int(sys.argv[1])
        else:
            print("none")
        print(arr)
except:
    print("invalid input")