import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
moves = open("./moves.json", encoding = "utf8")
move_data = json.load(moves)

def lang ():
    language = input("Please type your desired language: english, japenese, chinese, or french: ")
    language.lower
    x=[]
    for pokemon in data:
        print(pokemon["name"][language])
        x.append(pokemon["name"][language])
    return x
lang()

def typ ():
    type = input("What type of pokemon would you like? ")
    y=[]
    f=lang()
    type.capitalize()
    for pokemon in data: 
        if type in [pokemon["type"]]:
            print(f[pokemon["name"]])
            y.append
            print(y)
        return y
    if y == []:
        b= input("Nothing Found, would you like to try again? ")
        b.lower
        if b == "yes":
            while y == []:
                c = input("What type of pokemon would you like? ")
                c.capitalize()
                for pokemon in data: 
                    if c in [pokemon["type"]]:
                        print(f[pokemon["name"]])
                        y.append
                        print(y)
        return y
typ()

def lettero ():
    let1 = input("Type the first letter of the pokemon you want ")
    z = type()
    a = []
    let1.upper
    for pokemon in data:
        if let1 in z[pokemon["name"]][0]:
            print(pokemon["name"])
            a.append
        else:
            print("no match")
    return a
lettero()

""" if language == "english":
            print(pokemon["name"][language])
        elif language == "japenese":
            print("language selected: japenese")
        if language == "chinese":
            print("language selected: chinese")
        elif language == "french":
            print("language selected: french")
pokedex() """