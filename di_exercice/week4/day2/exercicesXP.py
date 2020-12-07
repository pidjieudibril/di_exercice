
# Exercise 1 : Favorite Numbers

my_fav_numbers = {25, 77, 92}

second_set = {1, 2}
print(my_fav_numbers | second_set)
print(type(my_fav_numbers))

my_fav_numbers.remove(25)
print(my_fav_numbers)
# on ne peut remove que les éléments originaux de l'ensemble
my_fav_numbers.pop()
print(my_fav_numbers)

friend_fav_numbers = {8, 94, 3, 12}

our_fav_numbers = my_fav_numbers | friend_fav_numbers

print(our_fav_numbers)

# Exercice 2 : Tuple

# Given a tuple with integers is it possible to add more integers to the tuple?

# no

# Exercise 3: Print A Range Of Numbers
for i in range(1, 21):
    print(i)


# Exercice 4 : Floats
# Can you think of another way of generating a sequence of floats?
x = 3.4
for i in range(10):
    print(x + 1)
# Create a list containing the sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5
# without hard-coding the sequence.
tableau = []
y = 1.5
tableau.append(y)
while y <= 5:
    y = y+0.5
    tableau.append(y)
print(tableau)
# print(tableau[::-1])
# Exercise 5: Shopping List

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")
basket.append('Kiwi')
basket.insert(0, "Apples")
print(basket.count('Apples'))
basket.clear()
print(basket)

# Exercise 6 : Loop
name = input('Enter a name : ')
while name != 'joseline':
    name = input('Enter a name : ')
# Exercise 7
liste = [1, 2, 3, 4, 6, 7, 8, 3]

"""for i in range(0, len(liste)):
    if (i == 0 or i%2 == 0):
        print(liste[i])
        
"""
i = 0
while i < len(liste):
    if i == 0 or i % 2 == 0:
        print(liste[i])
    i = i + 1

# Exercise 8
print('Les multiples de 3 sont :')
for i in range(3, 31):
    if i % 3 == 0:
        print(i)
# Exercise 9
print('Numbers between 1500 and 2700, which are divisible by 7 and multiples of 5.')
for i in range(1500, 2701):
    if i % 5 == 0 and i % 7 == 0:
        print(i)

# Exercise 10: Favorite Fruits
fruits = input('Enter your set of favorites fruits (separated by a space)  : ')

tab = fruits.split(' ')

fru = input('Enter the name of one fruit : ')

if fru in fruits:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy it too!')

# print(tab)
if len(tab) > 1:
    b = ' and '.join(tab)
    print('My favorites fruits are : {} '.format(b))

# Exercise 11: Who Ordered A Pizza ?
tab = []
prize = 10
pizza = input('Enter pizza topping (enter quit to stop) ')
print('THis topping will be added to your pizza')
tab.append(pizza)

while pizza != 'quit':
    print('This topping will be added to your pizza')
    pizza = input('Enter pizza topping (enter quit to stop) ')
    tab.append(pizza)
    prize = prize + 2.5
print('your topping are {} and the total prize is {}'.format(' and '.join(tab), prize))

# Exercise 12: Cinemax

famille = input('Enter the age of all the people who want a ticket separted by a space : ')

fam = famille.split(' ')

prix = 0

for i in range(0, len(fam)):
    if int(fam[i]) < 3:
        print('The prize is free for a kid of age {}'.format(int(fam[i])))
    elif int(fam[i]) in range(3, 13):
        print(' The prize for a kid of {} age is {}'.format(int(fam[i]), 10))
        prix = prix + 10
    else:
        print(' The prize for a kid of {} is {}'.format(int(fam[i]), 15))
        prix = prix + 15
print('The total prize is {}'.format(prix))

# Exercise 13 : Who Is Under 16?

users = ['Jo', 'Aure', 'Elsa', 'Orli']
long = len(users)
"""i = 0
while i in range(0,long):
    age = input('What is your age?')
    val = int(age)
    valeur = users[i]
    if val <= 15:
        users.remove(valeur)
    i = i+1
print(users)

for i in range(0, long):
    age = input('What is your age?')
    val = int(age)
    valeur = users[i]
    if val <= 15:
        users.remove(valeur)
        long = long - 1
print(users)
"""

# Exercise 14: Family Members

debut = input('Entrez un mot (Oui) pour debuter l\'enregistrement : ')
noms = []
while debut != 'exit':
    option = int(input('Enter an option number between 1 and 4 : '))
    if option == 1:
        name = input('add a name : ')
        noms.append(name)
    elif option == 2:
        val = input('Enter the name to remove : ')
        noms.remove(val)
    elif option == 3:
        print('The family members are {}'.format(noms))
    elif option == 4:
        print('BYE!!!')
        break
