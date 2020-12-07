# Exercise 1 : Concatenate Lists

liste1 = [1, 3, 4]
liste2 = [6]

b= liste1.__add__(liste2)
print(b)

# Exercise 2: Greatest Number
tab = []
a = int(input('Enter a number : '))
tab.append(a)
b = int(input('Enter a number : '))
tab.append(b)
c = int(input('Enter a number : '))
tab.append(c)

print('The greatest value is {}'.format(sorted(tab).pop()))

# Exercise 3 : The Alphabet

letter = input('Enter a string or the alphabet')

for i in range(0, len(letter)):
    if (letter[i] == 'a' or letter[i] == 'e' or letter[i] == 'i' or letter[i] == 'o' or letter[i] == 'u' or letter[i] == 'y'):
        print('{} is a voyel'.format(letter[i]))
    else:print('{} is a consonant'.format(letter[i]))

