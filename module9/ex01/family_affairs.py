#!/usr/bin/python3
def find_the_redheads(dupont_family):
    i = 0
    size = len(dupont_family)
    arr = []
    for x in range(size):
        if (list(dupont_family.values())[x] == "red"):
            arr.append(list(dupont_family.keys())[x])
    return (arr)
dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))