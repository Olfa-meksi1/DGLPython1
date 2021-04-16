import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import re
import string

def listAlphabet():
    # créer la liste des alphabets
    return list(string.ascii_lowercase)

def afficheDict(resultat):
    for cle, val in resultat.items():
        print(cle, ":", val)

def calculPourcent(resultat):
    for cle, val in resultat.items():
        resultat[cle] = (resultat[cle] / x) * 100

file = open("data.txt", "r")
text= file.read()
#print(text)
L = listAlphabet()
res = dict()
x=0
for elt in L:
    count = 0
    for lettre in text:
        if lettre == elt or lettre == elt.upper():
            count = count+1
            x = x+1            # pour calculer le nombre total des lettres
            res[elt]=count
        else:
            count = count
            res[elt] = count
    #print(str(count))
#afficheDict(res)
print("La somme totale des lettres est: ", str(x))

calculPourcent(res)
afficheDict(res)

plt.bar(res.keys(), res.values(), color ="g")
plt.title("Job 5")
plt.xlabel('Alphabets')
plt.ylabel("Pourcentage d'apparition")
plt.grid(True)
plt.show()

