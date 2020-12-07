# Reverse The Sentence
# Write a program to reverse the sentence wordwise.


# The corresponding function
def reverseSentence(sentence):
    return ' '.join(reversed(sentence.split(' ')))

print(reverseSentence('You have entered a wrong domain'))

# The no function version
sentence = input('Enter a sentence')
print(' '.join(reversed(sentence.split(' '))))
