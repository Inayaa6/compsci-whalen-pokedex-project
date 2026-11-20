import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
moves = open("./moves.json", encoding = "utf8")
move_data = json.load(moves)
""" 
def lang ():
    language = input("Please type your desired language: english, japenese, chinese, or french: ")
    language.lower
    x=[]
    for pokemon in data:
        print(pokemon["name"][language])
        x.append(pokemon["name"][language])
    return x   """  
#lang()

def typ ():
    type = input("What type of pokemon would you like? ")
    y=[]
    type.capitalize()
    for pokemon in data: 
        if type in pokemon["type"]:
            print(pokemon["type"])
            y.append
            print(y)
        else:
            print("no match")
typ()

""" def lettero ():
    let1 = input("Type the first letter of the pokemon you want ")
    z = typ()
    let1.upper
    for let1 in z:
        print(let1)
    return let1
lettero() """

""" if language == "english":
            print(pokemon["name"][language])
        elif language == "japenese":
            print("language selected: japenese")
        if language == "chinese":
            print("language selected: chinese")
        elif language == "french":
            print("language selected: french")
pokedex() """