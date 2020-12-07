# Exercise 1: Formula

import math
"""
c = int(input('Enter the value of C : '))
d = int(input('Enter the value of D : '))
h = int(input('Enter the value of H : '))
q = math.sqrt((2 * c * d) / h)
print('The value of Q is {}'.format(q.__trunc__()))

entre = input('Enter a serie of numbers separated by a coma : ')
tab = entre.split(',')

long = len(tab)
c = 50
h = 30
for i in range(0, long):
    d = int(tab[i])
    q = math.sqrt((2 * c * d) / h)
    print('The value of Q is {} for D = {}'.format(q.__trunc__(), d))
"""
# Exercise 2 : List Of Integers

#liste = (input('Entrez une liste de 10 chiffres séparés par une virgule')).split(',')
liste = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
print('The list of numbers : {}'.format(liste))
print('The list of numbers sorted in descending order (largest to smallest) : {}'.format(sorted(liste)[::-1]))
print('The sum of all the numbers : {}'.format(sum(liste)))
liste2 = [liste[0],liste[-1]]
print(liste2)
liste3 = []
for i in range(0,len(liste)):
    if liste[i] > 50 :
        liste3.append(liste[i])
print(liste3)
liste4 = []
for i in range(0,len(liste)):
    if liste[i] < 10 :
        liste4.append(liste[i])
print(liste4)

liste5 = []
for i in range(0,len(liste)):
    val = liste[i]**2
    liste5.append(val)
print(liste5)
