# Exercise 1
# Write a script that inserts an item at a defined index in a list.
import  math
def insertion(liste, index, item):
    if index < len(liste)-1:
        liste.insert(index,item)
    if index == len(liste):
        liste.append(item)
    return liste

a = [1, 2, 4, 5]

print(insertion(a, 2, 3))

#Exercise 2
#Write a script that counts the number of spaces in a string.

def counts(word):
    tab = list(word)
    return tab.count(' ')

mot = 'bonjour je suis fatiguée'

print(counts(mot))

#Exercise 3
#Write a script that calculates the number of upper case letters and lower case letters in a string.

def calcul(word):
    count1 = 0
    count2 = 0
    tab = list(word)
    for i in tab:
        if i.islower():
            count1 = count1+1
        elif i.isupper():
            count2 += 1
    return (count1, count2)

val1, val2 = calcul(mot)
print(val1)
print(val2)

# Exercise 4
# Write a function to find the max of a list

def findMax(liste):
    return sorted(liste).pop()

print(findMax(a))

# Exercise 5
# Write a function that return factorial of a number

def factorial(n):
    val = 1
    for i in range(2, n+1):
        val*=i
    return val

# Exercise 6
# Write a function to find the sum of an array without using the built in function:

def somme(liste):
    val = 0
    for i in range(0, len(liste)):
        val+=liste[i]
    return val

print(somme(a))


# Exercise 7
# Write a function that counts an element in a list (without using the count method):

def countJo(liste, element):
    val = 0
    for i in range(0, len(liste)):
        if liste[i] == element:
            val +=1
    return val


print(countJo(a,2))

# Exercise 8
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list

def normL2(liste):
    somme = 0
    for i in range(0,len(liste)):
        somme += (liste[i]**2)
    return math.sqrt(somme)

b = [1,2,2]
print(normL2(b))

#Exercise 9
#Write a function to find if an array is monotonic (sorted either ascending or descending)

def isMonotonic(liste):
    if liste[0] <= liste[len(liste)-1]:
        print('The list is sorted ascending')
    else:print('The list is sorted descending')

print(isMonotonic(a))

def isMono(liste):
    return liste == sorted(liste) or liste == sorted(liste)[::-1]

print(isMono([7,6,5,5,2,0]))
print(isMono([2,3,3,3]))
print(isMono([1,2,0,4]))

#Exercise 10
#Write a function that prints the longest word in a list.

def longWord(liste):
    long = 0
    position =0
    for i in liste:
        if len(i) >long:
            long = len(i)
            position = liste.index(i)
    return liste[position]

tab = ["bonjour", "bobo", "belle"]
print(longWord(tab))

# Exercise 11
# Given a list of integers and strings, put all the integers in one list, and all the strings in
# another one.

def separate(liste):
    listeint = []
    listestr = []
    for i in liste:
        if type(i) == str:
            listestr.append(i)
        elif type(i) == int:
            listeint.append(i)
    print('The list of integer is {}'.format(listeint))
    print('The list of strings is {}'.format(listestr))



tableau = ['bon', 2, 4, 'to', 5]
print(separate(tableau))

# Exercise 12
# Write a function to check if a string is a palindrome

def palindrome(word):
    test = True

    test = list(word)[0:len(word)//2] == list(word)[len(word)//2 +1:][::-1]
    return test

print(palindrome('radar'))
print(palindrome('John'))

# Exercise 13
# Write a function that returns the amount of words in a sentence with length > k


def sum_over_k(sentence, k):
    val = 0
    tab = sentence.split(' ')
    for i in tab:
        if len(i) > k :
            val+=1
    return val


sentence = 'Do or do not there is no try'
print(sum_over_k(sentence, 2))

# Exercise 14
# Write a function that returns the average value in a dictionary (assume the values are numeric)

def DicAvg(dictionary):
    long = len(dictionary)
    somme = 0
    for i in dictionary.values():
        somme+=i
    return somme/long

print(DicAvg({'a': 1,'b':2,'c':8,'d': 1}))

# Exercise 15
# Write a function that returns common divisors of 2 numbers

def CommonDiv(a,b):
    gcd = []
    if a <b :
        for i in range(2, a+1):
            if a%i == 0 and b%i == 0:
                gcd.append(i)
    else:
        for i in range(2, b+1):
            if a%i == 0 and b%i == 0:
                gcd.append(i)
    return gcd
print(CommonDiv(10,20))

#Exercise 16
#Write a function that test if a number is prime

def isPrime(number):
    compte = 0
    for i in range(2, number):
        if number % i == 0:
            compte +=1
    return compte==0

print(isPrime(11))

#Exercise 17
#Write a function that prints elements of a list if the index and the value are even

def weirdPrint(liste):
    tab = []
    for i in range(2,len(liste)):
        if i%2 == 0:
            tab.append(liste[i])
    return tab

print(weirdPrint([1,2,2,3,4,5]))

#Exercise 18
#Write a function that accepts an undefined numbers of keyworded arguments
# and return the count of different types

def TypeCount(**cvargrs):
    val = [0,0,0,0]
    for c, v in cvargrs.items():
        #print ("%s = %s" % (c,v))
        print("{}".format(type(v)))
        if type(v) =='int':
            val[0] += 1
        if type(v) =='bool':
            val[1] += 1
        if type(v) =='float':
            val[2]+=1
        if type(v) =='str':
            val[3] += 1

    return  val


print(TypeCount(abc = 123, efg = 456))

# Exercise 19
# Write a function that mimics the builtin .split() method for strings.
# By default the function uses whitespace but it should be able to take an argument for any character
# and split with that argument.

def splitJo(sentence, c = " "):
    tab = list(sentence)
    tab1 = []
    i = 0
    while i != len(tab)-1:
        mot = ''
        while tab[i]!=' ':
            mot+=tab[i]
            i+=1
        tab1.append(mot)
    return tab1


print(splitJo('bon tous'))
