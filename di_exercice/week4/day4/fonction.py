def say_hello(name="dibril"):
    print("salut a toi {}".format(name))

say_hello("jean piere")
say_hello()

def say_hello(username, language):
    if language == "EN":
        print("Hello "+username)
    elif language == "FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)

say_hello("Rick", "FR")

a=int(input("entrer la 1 valer"))
b=int(input("enter the second value"))

def calcul (c):
    addition =a+b
    soustration=a-b
    c=input("l'addition donne{} et la soustration donne{}".format(addition,soustration))
    return c


people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
filtered_object = list(filter(lambda s: len(s) <= 4, people))
b=list(map(lambda b: print("hello {}".format(b)),filtered_object ))












