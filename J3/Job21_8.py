import string

def listAlphabet():
    # créer la liste des alphabets
    return list(string.ascii_lowercase)

file = open("output.txt", "r")
text= file.read()

L = listAlphabet()
pos = dict()

#trouver la liste des positions d'une lettre (l) dans string (t)
trouver = lambda t, l:[i for i, c in enumerate(t) if c==l or c == l.upper()]

for elt in L:
    pos[elt] = trouver(text, elt)
print(pos)

# convertir les values de dic de string à entier
pos = {key: [int(value) for value in lpos] for key, lpos in pos.items()}

#incrémenter la liste de 1 (positions suivantes)
for key, value in pos.items():
    if isinstance(value, list):
        for index, elt in enumerate(value):
            value[index] = elt +1
        #print(value)
        pos[key]= value
print(pos)



for k in range(0,len(pos_lettre)):
    for elt in L:
        count = 0
        for i in range(len(text)):
            for j in range(len(pos_lettre[k])):
                if text[i] == elt and i == pos_lettre[k][j]:
                    count += 1
                    # print(str(count))
                else:
                    count = count
        r.append(count)
    res.append(r)


