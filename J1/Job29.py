
def draw_triangle(hight):
    nb_espace1 = hight - 1
    nb_espace2 = 0
    for i in range(hight):
        print(nb_espace1 * " " + "/" + nb_espace2 * " " + "\\")
        nb_espace1 -= 1
        nb_espace2 += 2
    print((hight * 2) * "-")


hauteur = int(input("Donner la hauteur du triangle: "))

##step 1
draw_triangle(hauteur)

## step 2
# hauteur = n
# nb_carat = 1
# nb_espace = hauteur - 1
#
# for i in range(hauteur):
#     print(nb_espace * " " + nb_carat * "*")
#     nb_carat+=2
#     nb_espace-=1
