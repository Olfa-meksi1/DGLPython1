import re
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import string

def listAlphabet():
    # créer la liste des alphabets
    return list(string.ascii_lowercase)

#trouver la liste des positions d'une lettre (l) dans string (t)
trouver = lambda t, l:[i for i, c in enumerate(t) if c==l or c == l.upper()]

file = open("output.txt", "r")
text= file.read()

L = listAlphabet()
pos=list()
pos_lettre = list()

for elt in L:
    pos.append(trouver(text, elt))
print("la liste des positions de chaque alphabet est: ",pos)

# for index, elt in enumerate(pos):
#     if isinstance(elt, list):
#         for index1, elt1 in enumerate(elt):
#             int(elt1)
#             pos[index1] = elt1 + 1
#print(pos)

for i in range(len(pos)):            # convertir la liste 2D de string à entier et l'incrémenter de 1
    '''fonction qui retourne la liste des positions suivantes à chaque lettre alphabet (dans l'ordre alphabetique) dans un texte'''
    for j in range(len(pos[i])):
        int(pos[i][j])
        pos[i][j]+= 1

print("la liste des positions +1 est: ", pos)

r = list()
res =list()
resultat = list()

# count = 0
# for i in range(len(text)):
#     for j in range(len(pos_lettre[0])):
#         if text[i] == "a" and i == pos_lettre[0][j]:
#             count = count +1
#             #print(str(count))
#         else:
#             count = count
# r.append(count)
# print(r)

# for elt in L:
#     count = 0
#     for i in range(len(text)):
#          for j in range(len(pos_lettre[0])):
#              if text[i] == elt and i == pos_lettre[0][j]:
#                 count = count +1
#                  #print(str(count))
#              else:
#                 count = count
#     r.append(count) #une liste compte l'apparition de elt après le "a"
# res.append(r) #une liste compte l'apparition de elt après le "a"
# print(r)
# print(res)

# for k in range(0,len(pos_lettre)):
# for elt in L:
#         count = 0
#         for i in range(len(text)):
#             for j in range(len(pos_lettre[k])):
#                 if text[i] == elt and i == pos_lettre[k][j]:
#                     count += 1
#                     # print(str(count))
#                 else:
#                     count = count
#         r.append(count)
#     res.append(r)
#
# print(len(r))
# print(res)  # il contient 26 lignes pour chaque alphabet (de 26 colonnes pour chaque alphabet) où chaque colonne indique l'occurence de chaque lettre après la lette "x"
#



######Remarques

#pos_lettre_int= [list(map(int,i)) for i in pos_lettre] # convertir la liste 1D de string à entier