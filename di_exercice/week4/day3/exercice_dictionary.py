#exercice 1 convertir les les listes en dictionaire


    # keys = ['Ten', 'Twenty', 'Thirty']
    # values = [10, 20, 30]
    # for items in zip(keys,values):
    # print(items)

# exercice 1 autre methode
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# hist = {}
# for i in range(len(keys)):
#    hist[keys[i]] = values[i]
# print(hist)
# exercice 1 autre methode
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
hist = {a: b for a, b in zip(keys, values)}
print(hist)

#exercice 2cinemax

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
a = 0
for i in family:
    if family[i]<3:
     print("" +i+" "+ "the ticket is free")
    elif family[i] < 12:

     print("" +i+" "+"the ticket is $10")
     a += 10
    else:
     print("" +i+" "+"the ticket is $15")
    a += 15
    print(a)



#exercice2bonus
family = {}
family["nom"]=input("entrer votre nom")
family["age"]=input("entrer votre age")
print(family)
#daily challenge day 3
msg= "mon secret est je mange "
x=list(string.ascii)
#exercice3
brand={
"name":"Zara",
"creation_date":1975,
"creator_name": "Amancio Ortega Gaona ",
"type_of_clothes":" men, women, children, home",
"number_stores": 7000,
"major_color":
     {"France":"blue", "Spain":"red"},
     "US":["pink", "green"]
}
print(brand)

