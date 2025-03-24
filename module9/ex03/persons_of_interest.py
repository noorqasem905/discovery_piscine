#!/usr/bin/python3
def famous_births(cl):
    sorted_scientists = sorted(cl.items(), key=lambda item: int(item[1]["date_of_birth"]))
    
    for scientist in sorted_scientists:
        name = scientist[1]["name"]
        birth_year = scientist[1]["date_of_birth"]
        print(f"Name: {name}, Date of Birth: {birth_year}")
    return (birth_year)
women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)