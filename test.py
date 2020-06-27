import json


data = {
    "First Trillianiare": {
        "name": "Nakarda Richards",
        "Networth": "1,378,834,745,658",
        "age": "19"
    },
    "Favorite Stuff": {
        "Favorite Games": "none",
        "Favorite Programming Langauge": "Python",
        "Favorite TV Series": "IDK"
    }
}


with open("test.json", "w") as write_file:
    json.dump(data, write_file)


print(data.items())
print(data.get("First Trillianiare"))
print(data.get("Favorite Stuff"))