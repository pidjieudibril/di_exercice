#exercice 1
def display_message():
    print("nous avons apris les fonction aujourd'hui")
display_message()

#exercice2
def favorite_book(title="Alice in Wonderland"):
    print("un de mes livre est :" +title)
favorite_book("mon plus beau livre")

#exercice 3
def describe_city(name_of_city,country="cameroun"):
    print(name_of_city +""+ "se trouve au " +country)
describe_city(name_of_city ="dla")
describe_city(name_of_city ="bfg")
describe_city(name_of_city ="bbshd")

#exercice 4
a="xl"
b="I love Python."
def make_shirt(taille = "10", message="mon jolie trico"):
    print("la taille de ma chemise est de : " + taille + "est le message a afficher est : " + message)

make_shirt()
make_shirt("l","j'aime se logo")

make_shirt(a,b)
make_shirt("xxl","autre message")

#exercice5
magicien_name=["dib","pid","etlui",]
def show_magicians(magicien):
    for i in magicien:
        print(i)
def make_great(list):
    grest_magician=["the great " + name for name in list]
    return grest_magician
new_magician=make_great(magicien_name)
show_magicians(new_magician)


