def Arrond(list_notes):
    for elt in list_notes:
        if (elt + 2.99) % 5 < 3:
            a = (elt + 3) % 5
            elt = elt + 3 - a
        else:
            elt = elt
        print(elt)

liste = list() #créer une liste vide


nb_stud = int(input("Donner le nombre des étudiants: "))

for i in range (0,nb_stud):
    x = int(input("Donnez une note pour l'étudiant " + str(i) + ":"))
    if x<0 or x>100:
        print("La note doit être comprise entre 0 et 100")
    else:
        liste.append(x)

print(liste)



Arrond(liste)

##for elt in liste:
##    if (elt+3)%5 ==0:
##        elt=elt+3
##    else:
##        elt = elt
##    print(elt)


