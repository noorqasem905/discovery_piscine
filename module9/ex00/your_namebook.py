#!/usr/bin/python3
def array_of_names(persons):
    i = 0
    size = len(persons)
    arr = []
    for x in range(size):
        arr.append(list(persons.keys())[x])
    for x in range(size):
        arr[x] += " " +(list(persons.values())[x]) 
    return (arr)
persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))