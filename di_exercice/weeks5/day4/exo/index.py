import json

family = 'file.json'
with open(family, 'r') as file_obj:
    my_family = json.load(file_obj)



a=my_family["children"][0]["favorite_color"]="red"
b=my_family["children"][1]["favorite_color"]="red"
print(a)
print(b)

print(my_family)

with open(family, 'w') as file_obj:#ouvre le ficher en ecriture
    json.dump(my_family, file_obj, indent = 2, sort_keys=True)
