import json
a = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
family= 'file.json'

with open(family, 'w') as file_obj:#ouvre le ficher en ecriture
    json.dump(a, file_obj, indent = 2, sort_keys=True)

a["children"][0]["favorite_color"]="red"
a["children"][1]["favorite_color"]="red"
print(a)

#r lire a linterieur
#w metre a l'interieur
#a ouvrir un fichier sans rien supprimer
#