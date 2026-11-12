import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
print(data[0])

def pokedex ():
    y = input("Please type your desired language: english, japenese, chinese, or french: ")
    y.lower
    if y == "english":
        print((data, ["name"["english"]]))
    if y == "japenese":
        print("language selected")
    if y == "chinese":
    else:

pokedex()