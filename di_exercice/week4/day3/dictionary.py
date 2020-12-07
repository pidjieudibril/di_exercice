my_name = {
  'name': 'dib',
  'age': 4,
    "username":"pid"
}

print( my_name['username'] )

etudiant={
    "nom":"joseph ateba",
    "age":35,
    "note":[14,20,15],
    "enfant":{"nom":"bebe joseh","age":4}}

print(etudiant["nom"])
print(etudiant["note"][1])
print(etudiant["enfant"]["nom"])


maliste = list(etudiant)
print(maliste)

li= [x for x in range(101) if x%3==0]
print(li)
for i in range(1, 3):
    print(i)

print('The for loop is over')
