class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age


mon_chatnoir = Cat(name="chatnoir",age=10)
mon_chatblanc = Cat(name="chatblanc",age=7)
mon_chatrouge = Cat(name="chatrouge",age=15)


#def myfunc():
    #if mon_chatblanc.age<mon_chatnoir.age<mon_chatrouge.age:
        #return mon_chatrouge
    #elif mon_chatrouge.age<mon_chatnoir.age<mon_chatblanc.age:
        #return mon_chatblanc
    #else:
        #return mon_chatnoir
#test=myfunc()
#print("le chat le plus age est:" + test.name)
"""
def oldest(*args):
    return max(args key=lambda cat:cat.age)
    """
"""
def oldest(*args):
    old = args[0]
    for cat in args:
        if cat.age>old.age:
            old=cat
    return old



oldest()
"""
#exercice2
class Dog():
    def __init__(self,name,height):
        self.mon_nom=name
        self.ma_taille=height

    def bark(self):
        print("{} va woof!".format(self.mon_nom))

    def saut_de_methode(self):
        x=self.ma_taille*2
        print("saut {} cm de haut".format(x))

    def autre(selh):
        print("le non de son chien est: {} , et sa taille es :{} cm".format(selh.mon_nom,selh.ma_taille))

    def s(self):
        print("le non de son chien est: {} , et sa taille es :{} cm".format(self.mon_nom, self.ma_taille))
attribut_instance = Dog("dibril",65)
davids_dog=Dog("rex",50)
sarahs_doc =Dog("Teacup",20)

attribut_instance.bark()
attribut_instance.saut_de_methode()
davids_dog.autre()
sarahs_doc.s()
# regarde le if de l'exercice 2

# exercice 3

class Song():
    def __init__(self,lyrics):
        self.ma_munsique=lyrics
    def sing_me_a_song(self):
        non=" ma maillieur musique"
        index=0
        while index<len(non):
            print("nom[index]")

