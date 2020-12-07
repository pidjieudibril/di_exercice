#exercice1
print("hello word \n"*4)

#exercice 2
resultat=(99^3) * 8
print(resultat)

#exercice 3
a=bool(5<3)
print(a)
b=bool(3 == 3)
print(b)
c=bool(3 == "3")
print(c)
d=bool("3" > 3)
print(d)
e=bool("Hello" == "hello")
print(e)

# exercice 5
computer_brand="bell"
print(" I have a razer " + computer_brand + " computer ")

name="pidjieu dibril"
age= 30
shoe_size=40
info= (" je m'appelle {} i have {}year old and i shoe {} ")
print(info.format(name,age,shoe_size))

#exercice 6
n = int(input("Entrez un nombre: "))
if (n % 2) == 0:
   print("{0} est Paire".format(n))
else:
   print("{0} est Impaire".format(n))

# exercice 7

n=input("enter your name")
liste= ["jacque","paul","jean pierre"]
if n in liste:
 print("True,"+ n+ "est trouvé dans la liste : et voici ceux qui sont dans la liste " , liste)
elif n not in liste :
    print("false," + n + "n'est pas encore dans la  liste : et voici ceux qui sont dans la liste ", liste)


    #exercice 8

    # CONSTANTE

    UN_POUCE = float(2.54)  # 1 pouce = 2.54 cm
     # VARIABLES

    valeur = float()  # valeur de l longueur saisie au clavier

    unite = str()  # valeur de l’unite saisie au clavier

    longueurEnPouce = float()  # longueur convertie en pouces

    longueurEnCm = float()  # longueur convertie en centimètres


    print("Conversion d’une mesure en pouces ou en centimètres")
    # 1.Saisir la longueur (valeur + unité)

    valeur = float(input("Saisir la valeur de la longueur : "))

    unite = input("Saisir l’unité : p (pouce) , m (metre) , c (centimetre) ")

    unite = unite.upper()  # conversion en majuscule pour faciliter les tests

     # 2.Calculer la longueur en pouces et en centimètres

    if unite == "P":  # la longueur a été saisie en pouces

     longueurEnPouce = valeur
     longueurEnCm = valeur * UN_POUCE
    elif unite == "M":  # la longueur a été saisie en mètres

        longueurEnPouce = 100 * valeur / UN_POUCE

        longueurEnCm = 100 * valeur
    elif unite == "C":  # la longueur a été saisie en centimètres

     longueurEnPouce = valeur / UN_POUCE

     longueurEnCm = valeur
    else:  # unité non reconnue

     longueurEnPouce = 0
     longueurEnCm = 0
     # 3.Afficher le résultat

     print("Valeurs brutes :", longueurEnPouce, "pouces et", longueurEnCm, "cm")

     print("Valeurs arrondies :",

     format(longueurEnPouce, ".3f"), "pouces et",

     format(longueurEnCm, ".3f"), "cm")


#exercice xp gold
#exercice 1
#exercice1
print("hello word \n"*4, "\n I love python\n"*4)

#exercice 2