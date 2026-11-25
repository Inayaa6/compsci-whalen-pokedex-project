import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
moves = open("./moves.json", encoding = "utf8")
move_data = json.load(moves)

def lang ():
    language = input("Please type your desired language: english, japenese, chinese, or french: ")
    language= language.lower()
    x=language
    for pokemon in data:
        print(pokemon["name"][language])
    return x
lang()

def typ ():
    type = input("What type of pokemon would you like? ")
    y=[]
    f=lang()
    type = type.capitalize()
    for pokemon in data:
        if type in pokemon["type"]:
            print(pokemon["name"][f])
            y.append(pokemon["name"][f])
        return y
#typ()
#I added random [] by accident

def lettero ():
    let1 = input("Type the first letter of the pokemon you want ")  
    a = []
    let1.upper()
    for pokemon in data:
        try:
            if let1 in pokemon["name"][0]:
                print(pokemon["name"])
                a.append(pokemon["name"])
        except KeyError:
            continue
        
    return a
lettero()

""" def practice():
    users = [
        {"name": "Alice", "role": "admin"},
        {"name": "Bob", "role": "user"},
        {"name": "Charlie", "role": "admin"},
        {"name": "David"},
        {"name": "Eve", "role": "moderator"}
]
    for users in users:
        try:
            if "admin" in users["role"]:
                print(users["name"])
        except KeyError:
            continue
practice() """

""" if language == "english":
            print(pokemon["name"][language])
        elif language == "japenese":
            print("language selected: japenese")
        if language == "chinese":
            print("language selected: chinese")
        elif language == "french":
            print("language selected: french")
pokedex() """