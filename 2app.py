import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
def pokedex ():
    language = input("Please type your desired language: english, japenese, chinese, or french: ")
    language.lower
    for pokemon in data:
        print(pokemon["name"][language])
    type = input("What type of pokemon would you like? ")
    type.lower
    type.upper[0]
    for pokemon in data:
        print(pokemon[language]["type"][type])
pokedex()


""" if language == "english":
            print(pokemon["name"][language])
        elif language == "japenese":
            print("language selected: japenese")
        if language == "chinese":
            print("language selected: chinese")
        elif language == "french":
            print("language selected: french")
pokedex() """