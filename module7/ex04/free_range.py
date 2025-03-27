#!/usr/bin/env python3
import sys
try:
        i = 0
        size = len(sys.argv)
        if size == 3:
            if int(sys.argv[1]) <= int(sys.argv[2]):
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
                print(arr)
            else:
                print("none")
        else:
            print("none")
except:
    print("Invalied Argments", file= sys.stderr)