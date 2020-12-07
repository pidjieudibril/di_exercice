class nourriture():
    def __init__(self,name="jean",weight="10kg"):#voici mon constructeur
       print("definition de la classe nourriture")
       self.nom=name #ses variable
       self.poids=weight

    def presentation(self):
        print("Nom :{} et poids :{}".format(self.nom,self.poids))
moninstance = nourriture() #instance de la classe
nou=nourriture(name="jeanne",weight="pat")

class Point(): #definition de la calsse
    def __init__(self, x, y):#initialisation des valeur x et y avec le constructeur init
        self.x = x # ses variable
        self.y = y

## create an instance of the class
p = Point(3,4)

## access the attributes
print("p.x is:", p.x)
print("p.y is:", p.y)


class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        #Analyse the line below
        print(self)

computer1 = Computer() #on creer une instance de la classe computer
computer1.brand = "Apple" #ajouter l'attribut brand a la classe computer
computer1.color="bleu"
print(computer1.brand,computer1.color)

computer2 = Computer()

Computer.description(computer2, "Mark")
# IS THE SAME AS:
computer2.description("Mark kdj")