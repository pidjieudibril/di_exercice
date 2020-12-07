class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Autrerase(Cat):
    def color(self,white):
        return f"{white}"


my_cats=Bengal("mian",5)
my_cats1=Chartreux("djic",16)
my_cats2=Autrerase("black_cat",10)

my_pets=Pets([my_cats1,my_cats2,my_cats])
my_pets.walk()


#exercice 2
class Dog():
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
        self.sound="whouuf"

    def bark(self):
        print(f"sa facon d'aboyer {self.sound}")
    def run_speed(self):
        a=(self.weight/ self.age) * 10
        return a
    def fight(self,other_dog):
      if  self.run_speed()<other_dog.run_speed():
          return f"le chien {other_dog.name} a gagné "

      elif other_dog.run_speed()< self.run_speed():
          return   f"le chien {self.name} a gagné "



dog1=Dog("yaky",12,50)
dog2=Dog("yan",15,60)
dog3=Dog("djic",7,20)
print(dog3.fight(other_dog=dog2))


#exercice3

