#!/usr/bin/python3
import sys

def add_one(st):
    return (st + 1)
try:
    e = 0
    print("The Number: ",e)
    e = add_one(e)
    print("Number After Added 1: " ,e)
except Exception as e:
    print(f"ERROR: {e}")
