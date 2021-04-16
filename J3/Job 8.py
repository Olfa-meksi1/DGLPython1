import re
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

#def motLettreN(n):      ## Nombre de mots qui contiennent n lettres


def listeEntierTester(n):
    liste = list()
    for i in range(1,n+1):
        liste.append(i)
    return liste

def afficheDict(resultat):
    for cle, val in resultat.items():
        print(cle, ":", val)

def calculPourcent(resultat, x):
    for cle, val in resultat.items():
        resultat[cle] = (resultat[cle] / x) * 100


file = open("data.txt", "r")
liste_data =re.findall(r"[\w']+", file.read())  # liste contenant tout le mot dans le fichier
#print(liste_data)

L = listeEntierTester(19)
#print("L est: ", L)
res = dict()
for elt in L:
    count = 0
    for elt1 in liste_data:
        if len(elt1) == elt:
            count = count +1
            res[elt] = count
        else:
            count = count
            res[elt] = count

afficheDict(res)

calculPourcent(res, len(liste_data))
afficheDict(res)

plt.bar(res.keys(), res.values(), color ="g")
plt.title("Job 8")
plt.xlabel("Taille d'un mot")
plt.ylabel("Apparition d'un mot de taille x en %")
plt.grid(True)
plt.axis([0, 19, 0, 16])
plt.show()
