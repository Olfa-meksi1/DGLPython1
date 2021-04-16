import re

#méthode 1
file = open("data.txt", "r")
#L = file.readlines() # liste des ligne dans le fichier
#F=(file.read().split("."))    # liste des phrases dans le fichier
count = len(file.read().split(" "))
#print(str(len(F[1])))
print("Le nombre de mot est: ", str(count))
file.close()

#Méthode 2
file = open("data.txt", "r")
txt = file.read()
x = re.split("\s", txt)
#print(x)
count1 = len(x)
print("Le nombre de mot est selon la Regex est : ", str(count1))
file.close()

