print("hello word")
a = 10
b=5
c=a+b
print(c)
c = a/b
print(c)
d=b%a
print("the number is :")

print("Hello world\nMy name is Rick")


print("Peace on the\tWORLD")
Name = input("please star your name :")
Age=input("please star your age :")

print('your age and your name is {}{}'.format(Name,Age))
n = int(input("entrer un nombre "))
if n%2==0:
    print("{0} est pair".format(n))
else:
    print("{0} est impaire".format(n))


age = input("enter your age please")
age=int(age)

if age > 90:
    print(" good morning the old")
elif age < 10:
    print("bonjour bb")
else:
    print("you don\'t have a age")

my_hobbies = ["sport", "code", "food", "icecreams", "netflix"]
if "code" in my_hobbies:
    print("Hello world")





n = int(input("Entrez un entier [1 .. 100] : "))


while n<100:
    n +=1
if n%3==0 :

    print("fizz")

elif n%5==0 :

    print("buzz")

elif n%3==0 and n%5==0 :
    print("fizzbuzz")

else:
    print("le nombre n'est pas compris entre 1 et 100")
