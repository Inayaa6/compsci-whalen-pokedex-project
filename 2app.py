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
        x.append
lang()

def typ ():
    type = input("What type of pokemon would you like? ")
    y = def lang(x)
    w= [] 
    type.lower
    type[0].upper
    for y in type:
        print(moves["type"][type])
        w.append
typ()

def lettero ():
    let1 = input("Type the first letter of the pokemon you want ")
    z = def typ(w)
    let1.upper
    for z in let1:
        print(let1)
lettero


""" if language == "english":
            print(pokemon["name"][language])
        elif language == "japenese":
            print("language selected: japenese")
        if language == "chinese":
            print("language selected: chinese")
        elif language == "french":
            print("language selected: french")
pokedex() """