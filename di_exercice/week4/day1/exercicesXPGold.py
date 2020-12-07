# Exercice 1 : Hello World-I Love Python


print('{}{}'.format('Hello world \n'*4, 'I love python\n'*4))

# Exercice 2 : What Is The Season ?

month = input('Enter a month\' number (1,12) : ')
if int(month) in range(3,6):
    print('It\'s is Spring season')
if int(month) in range(6,9):
    print('Summer! Where is your bikini?')
if int(month) in range(9,12):
    print('Autumn!')
if int(month) in range(12, 3):
    print('Ouch!! Winter season. Hope you have some few good coats')
