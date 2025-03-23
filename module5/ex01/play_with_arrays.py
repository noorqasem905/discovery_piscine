#!/usr/bin/python3
arr_org = [2, 8, 9, 48, 8, 22, -12, 2]
arr_cpy = [None] * len(arr_org)
for i in range(len(arr_org)):
    arr_cpy[i] = arr_org[i] + 2
print(arr_org)
print(arr_cpy)