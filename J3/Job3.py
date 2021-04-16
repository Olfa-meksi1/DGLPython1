import re

file = open("data.txt", "r")
liste_data =re.findall(r"[\w']+", file.read())  # liste contenant tout le mot dans le fichier
#print(liste_data)
#print(str(len(liste_data[0]))

n = int(input("Donner un nombre entier: "))
nb_apparition =0


for elt in liste_data:
    if len(elt) == n:
        #print(elt)
        nb_apparition = nb_apparition + 1
    else:
        nb_apparition =nb_apparition
print("Dans ce fichier, il y a ", str(nb_apparition), " mots qui contiennent", str(n), "lettres!")