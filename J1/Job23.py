
##tab = []

##def draw_rectangle(width,hight):
##    for i in range(width):
##        tab.append("-" * hight )
##        print(tab[i])


def draw_rectangle(width,hight):
    print("|" + (width-2)* "-" + "|")
    for i in range (hight-2):
        print("|" +  (width-2) * " " + "|")
    print("|" + (width-2) * "-" + "|")


draw_rectangle(5,6)

	




