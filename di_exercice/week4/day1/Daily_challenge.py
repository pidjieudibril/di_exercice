import random
chaine=str(input("entrer une chaine de caractere"))
if len(chaine) < 10:
    print("string not long enough")
elif len(chaine)>10:
    print("string long enough")

    print(chaine[0])
    print(chaine[-1])

    print(chaine[0:str:str-1])


    chaine=list(chaine)
    random.shuffle(chaine)
    chaine="".join(chaine)
    print(chaine)
#ou encore
    " ".join(random.sample(chaine, len(chaine)))

    eleve=[ "dibbril", " patair", "nanou" ,]
   # eleve
    eleve[0]=10 #changer diberil par 10
   # eleve.append(false) #ajouter false dans la liste
   # eleve
    type(eleve) # retourne le type list
    eleve.remove("nanou")

    list1 = [5, 10, 15, 20, 25, 50, 20]
    list2=list1.index(20)
    list1[list2]=200

    q=list()
    q.append(4)
    #q
    s=set()
    s.append(8)#faux
    s.add(8)
    s


    n = int(input("entrer un nombre entre 1 et 12"))
    a = range( 1 , 13)
    for i in a:
        print("la table de multiplication de {} * {} = {}".format(n,i,i*n))




