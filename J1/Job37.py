##from itertools import permutations
import locale
locale.setlocale(locale.LC_ALL, "")

def Permute(string):
    if len(string) == 0:
        return ['']
    prevList = Permute(string[1:len(string)])
    nextList = []
    for i in range(0,len(prevList)):
        for j in range(0,len(string)):
            newString = prevList[i][0:j]+string[0]+prevList[i][j:len(string)-1]
            if newString not in nextList:
                nextList.append(newString)
    return nextList

Ch = input("Donner un seul mot sans espace ni aucun autre caractère que les 26 lettres de l'alphabet: ")

l= len(Ch)
print(" La longueur de la chaine saisie est: " + str(l))

stringlist = Permute(Ch)

#print(sorted(stringlist))

k =  0
while k < len(stringlist):
     for i in range(l-1):
         if Ch[i] == stringlist[k][i] and Ch[l-2]== stringlist[k][l-1] and Ch[l-1]== stringlist[k][l-2]:
             Ch = stringlist[k]
             print(Ch + ": est le mot le plus proche")
             break
         else:
             k= k+1


# while k < len(stringlist):
#      if Ch == stringlist[k]:
#          print(stringlist[k] + ": est le mot d'origine")
#          k = k+1
#      else:
#          for i in range(l-1):
#              if Ch[i] == stringlist[k][i] and Ch[l-2]== stringlist[k][l-1] and Ch[l-1]== stringlist[k][l-2]:
#                  Ch = stringlist[k]
#                  print(Ch + ": est le mot le plus proche")
#              else:
#                  k= k+1
#              break



# char1 = Ch[l-1]
# print(char1)
# char2 = Ch[l-2]
# print(char2)
#
# Ch1 = Ch[0:l-2]
# Ch2 = Ch1 + char1 + char2
#
# print(Ch2)



##str = ['\n'.join(p) for p in permuations()]

