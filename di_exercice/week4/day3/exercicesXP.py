# Exercise 1 : Convert Lists Into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = str(dict(zip(keys,values)))
for elt in my_dict:
    print(elt, end='')

# Exercise 2 : Cinemax #2

family = {'rick': 43, 'beth': 13, 'morty': 5, 'summer': 8}
prize = 0
for i in family:
    if int(family[i]) < 3:
        print('\n For {}, the ticket is free'.format(i.capitalize()))

    elif int(family[i] in range(3, 13)):
        print('\n For {}, the ticket is 10 $'.format(i.capitalize()))
        prize = prize + 10

    elif int(family[i]) > 12:
        print('\n For {}, the ticket is 15 $'.format(i.capitalize()))
        prize += 15
print('\n The total prize for the whole family is {}'.format(prize))

noms = input('Enter the list of family member\'s names separated by a space : ')
age = input('Enter the list of family members\'s ages correspondant : ')
ages = age.split(' ')
agess = []
for i in range(0, len(ages)):
    agess.append(int(ages[i]))

family = str(dict(zip(noms.split(' '), agess)))
print(family)

# Exercise 3: Zara

brand = {
    'name': 'Zara' ,
    'creation_date' : 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {'France' : 'blue', 'Spain' : 'red', 'US' : ['pink', 'green'] },
}

brand['number_stores'] = 2
print('The type of clients of Zara are {}'.format(brand['type_of_clothes']))
brand['country_creation'] = 'Spain'
print(brand)
brand['international_competitors'].append('Desigual')
print(brand)
del brand['creation_date']
print(brand['international_competitors'][-1])

print('The major clothes\' colors in the US are {}'.format(' and '.join(brand['major_color']['US'])))
print(len(brand))
print(brand.keys())

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000,
}

brand.update(more_on_zara)
print(brand)

print(brand['number_stores'])

# the number of stores have been updated

# Exercise 4 : Disney Characters

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
numbers = [i for i in range(1,5)]

disney_users_A = str(dict(zip(users, numbers)))
print(disney_users_A)

disney_users_B = str(dict(zip(numbers,users)))
print(disney_users_B)

disney_users_C = str(dict(zip(sorted(users),numbers)))
print(disney_users_C)

tab = [i for i in users if i.count('i')> 0]
print(str(dict(zip(tab, numbers))))

tab1 = [i for i in users if i[0] == 'm' or i[0] == 'p']
print(str(dict(zip(tab1, numbers))))
