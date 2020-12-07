file=open("fichier.txt","r")

# utiliser readlines pour lire toutes les lignes du fichier
# La variable "lignes" est une liste contenant toutes les lignes du fichier
lines = file.readlines()
print(lines[6])
print(lines[6])
# fermez le fichier après avoir lu les lignes
file.close()
# Itérer sur les lignes
for line in lines:
    print(line.strip())
