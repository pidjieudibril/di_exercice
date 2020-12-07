# Exercice 1 : Hello world

sentence = 'Hello world \n'

print(sentence * 4 )

# Exercice 2 : Some math
# 1- calculate
valeur = (99^3)*8
print(valeur)

#Exercice 3: What is the ouput ?

print(5 < 3)
print(3 == 3)
print(3 == "3")
print('3' == 3)
print("Hello" == "hello")

# Exercice 4 : Your computer brand

# 1 - Create a variable called computer_brand that contains the brand of your computer.
computer_brand = 'Dell'
# 2 - Insert and print the above variable in a sentence,like "I have a razer computer".
print('I have a {} computer.'.format(computer_brand))

#Exercice 5 :Your information

name = 'Joseline'
age = 27
shoe_size = 40
info = 'My name is {}. I\'m {} and my shoe size is {}.'.format(name, age, shoe_size)
print(info)

# Exercice 6 : Odd or Even
valeur = input(' Enter an integer : ')
if int(valeur)%2 == 0:
    print('{} is even.'.format(valeur))
else: print('{}  is odd'.format(valeur))

# Exercice 7 : What’s Your Name ?

nom = input('Enter your name ')
if(name == 'joseline'):
    print('We are bombom!!')
else: print('Sorry {} is not the same as joseline'.format(nom))

# Exercice 8 : Tall Enough To Ride A Roller Coaster

height = input('Enter your height in inch ')
taille = int(height)*2.54
if(taille >= 145):
    print('you can ride a roller coaster!!')
else:print('you are too short to ride a roller coaster')
