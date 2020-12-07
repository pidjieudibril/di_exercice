# Exercise 1: Birthday Look-Up

birthdays = {
    'Jo' : '1992/11/25',
    'Orli': '1994/08/25',
    'Aure': '1994/08/25',
    'Clovis': '1997/04/18',
    'Carine': '1986/04/09',
}

print('Welcome!')
#print('You can look up the birthday of the people in the list!')
#name = input('Enter a person\' name : ')
#print('The birthday of {} is {}'.format(name, birthdays[name]))

#Exercise 2: Birthdays Advanced
print('The names are : ')
for i in birthdays:
    print(i, end=' ')

print('\n You can look up the birthday of the people in the above list!')
name = input('Enter a person\' name : ')
ex = False
for i in birthdays:
    if i == name:
        ex = True
        break


if ex == True:
    print('The birthday of {} is {}'.format(name, birthdays[name]))
else:
    print('Sorry, we don\'t have birthday information for {}'.format(name))
