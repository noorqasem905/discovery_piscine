#!/usr/bin/python3
i = 0
j = 0
i = int(i)
j = int(j)
result = 0
result = int(result)
while i <= 10:
    result = i
    print("Table of " + str(i) + ": ", end="")
    while j <= 10:
        result = j * i
        print(result, end=" ")
        j += 1
    print()
    i += 1
    j = 0