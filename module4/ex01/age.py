#!/usr/bin/python3
i = 1
i = int(i)
enter = input("Please tell me your age: ")
print("You are currently " + str(enter) + " years old.")
while i <= 3:
    print("In "+ str(i * 10) +" years, you'll be " + str(int(enter) * int(i))  + " years old.")
    i += 1 