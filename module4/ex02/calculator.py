#!/usr/bin/python3
try:
first_num = int(input("Give me the first number: "))
second_num = int(input("Give me the second number: "))

print("Thank you!")
print(f"{first_num} + {second_num} = {first_num + second_num}")
print(f"{first_num} - {second_num} = {first_num - second_num}")
print(f"{first_num} / {second_num} = {first_num / second_num:.2f}")
print(f"{first_num} * {second_num} = {first_num * second_num}")
except:
    print("ERROR")