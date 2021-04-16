import re
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import string


def listAlphabet():
    # créer la liste des alphabets
    return list(string.ascii_lowercase)

def afficheDict(resultat):
    for cle, val in resultat.items():
        print(cle, ":", val)

def calculPourcent(resultat, x):
    for cle, val in resultat.items():
        resultat[cle] = (resultat[cle] / x) * 100

file = open("data.txt", "r")
liste_data =re.findall(r"[\w']+", file.read())  # liste contenant tout les mots dans le fichier
#print(text)
L = listAlphabet()
res = dict()

for elt in L:
    count = 0
    for elt1 in liste_data:
        if elt1[0] == elt or elt1[0] == elt.upper():
            count = count+1
            res[elt]=count
        else:
            count = count
            res[elt] = count

#afficheDict(res)

calculPourcent(res, len(liste_data))
afficheDict(res)

plt.bar(res.keys(), res.values(), color ="g")
plt.title("Job 13")
plt.xlabel("Alphabet")
plt.ylabel("Apparition d'un lettre au début d'un mot en %")
plt.grid(True)
plt.show()