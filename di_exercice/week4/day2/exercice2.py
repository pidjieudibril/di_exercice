

my_fav_numbers={13}
my_fav_numbers.add(14)
my_fav_numbers.add(12)
print(my_fav_numbers)

l=list(my_fav_numbers)
print(l)
del l[-1]
print(l)

friend_fav_numbers={13,4,6}
d=list(friend_fav_numbers)
print(d)
our_fav_numbers= d + l

print(our_fav_numbers)

#exercice 2
t = ('Ben',34,'Lille')
t = t + ('Computer Scientist',)
print(t)

#exercice 3

for i in range(20):
    print(i)

#exercice 4



#import numpy as np
#for i in np.arange(1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5):
  #  print(i)

#quelque exemple utilisation des tableau
li= [x for x in range(10)]
print(li)
li= [x*2 for x in range(20) if x>10]
print(li)
li= [x*2 for x in range(20)]


#exercice 5

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.append("Kiwi")
basket.insert(0,"pommes")
basket.count("pommes")
basket.clear()
print(basket)

#exercice 6

nom = "jean"
i=input("entrer votre nom")
while i != nom:
    i = input(" entrer de nouveau votre nom")

    #exercice 7

    liste=[6,7,16,23,4]

    while i<len(liste):
        i = 0
        x = liste.index(i)
        if i % x==0:
            print(i)
        else:
            i += 1









    #exercice7