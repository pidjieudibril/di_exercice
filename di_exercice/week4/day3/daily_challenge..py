alphabet="abcdefghijklmnopqrstuvwxyz"
key=3
newMessage=""#permet de stocker le nouveau message chiffré
message=input("pleace enter a message :").lower()#transforme l'entrer en minuscule avant de lancer la recherche
for character in message:#permet de repecter pour chaque caractere dans le message
    if character in alphabet:# permet de prendre en compte les caractere speciaux
        position =alphabet.find(character)#pour trouver la position du caractere
        newPosition = (position + key) % 26#pour chiffré faut ajouter la clé, puis retourner a 0 apres la position 26
        newCharacter =alphabet[newPosition]#afficher la lettre a la nouvelle position
        newMessage += newCharacter#ajouter chaque caractere chiffré dans la variable new message
    else:
        newMessage += character
print("your new message is :", newMessage)


message=input("pleace enter a message :")
for character in message:
    if character in alphabet:
        position =alphabet.find(character)
        newPosition = (position - key) % 26
        newCharacter =alphabet[newPosition]
        newMessage += newCharacter
    else:
        newMessage += character
print("your new message is :", newMessage)