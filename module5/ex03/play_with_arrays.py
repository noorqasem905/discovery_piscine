#!/usr/bin/env python3
size = 0
arr_org = ([2, 8, 9, 48, 8, 22, -12, 2])
arr_cpy = [x + 2 for x in arr_org if x > 5]
for x in arr_cpy:
    for y in arr_cpy:
        if x == y:
            size += 1
        if size > 1:
            arr_cpy.remove(x)
            size = 0
    size = 0
print(arr_org)
print(arr_cpy)