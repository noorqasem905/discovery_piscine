#!/usr/bin/python3
size = 0
size = int(size)
arr_org = [2, 8, 9, 48, 8, 22, -12, 2]
arr_cpy = [x + 2 for x in arr_org if x > 5]
print(arr_org)
print(arr_cpy)