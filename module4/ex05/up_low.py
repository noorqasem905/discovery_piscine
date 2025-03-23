#!/usr/bin/python3
i = 0
enter = input("")
i = int(i)
while len(enter) > i:
    if enter[i].isupper():
        print(enter[i].lower(), end="")
    elif enter[i].islower():
        print(enter[i].upper(), end="")
    else:
        print(enter[i], end="")
    i += 1
