# Exercise 3

print(3<=3<9)
print(3 == 3 == 3)
print(bool(0))
print(bool(5 == "5"))
#print(bool(1))
print(bool(4 == 4) == bool("4" == "4"))
print(bool(bool(None)))

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

#Exercice 4 : How Many Characters In A Sentence ?

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text)-my_text.count(' '))

# Exercice 5 : Longest Word Without A Specific Character
sent = input(" Enter the longuest sentence you can without 'A' inside ")
count = 0
if sent.count('a')>0:
    print("Your sentence have 'A' inside ")
    while sent.count('a')>0:
        print("Your sentence have 'A' inside ")
        sent = input(" Enter the longuest sentence you can without 'A' inside ")
else:
    print('congrats!!')
    count = count + 1
    print(count)


