# Mini-Project #2 - Hangman

import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)
longWord = len(word)
print('The choosen word is {}'.format('*'*longWord))
wordCache = list('*'*longWord)
tab = list(word)
tab1 = []

while wordCache.count('*')>0:
    letter = input('Type a letter : ')
    if letter in tab:
        wordCache[tab.index(letter)] = letter
        tab[tab.index(letter)] = ''
        print(wordCache)
    else:
        print('The letter {} is not in the word. Enter another letter'.format(letter))
        #letter = input('Type a letter : ')

