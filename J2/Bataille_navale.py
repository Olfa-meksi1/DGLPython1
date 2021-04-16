Mer = 0
Bat = 1
Tir = 2
Deb = 3

class Grille():
    def __init__(self, height, width):
        self.height = height
        self.width  = width
        self.cases = [[0 for x in range(width)] for x in range(height)]

    def valCase(self, i, j):
        #pour accéder à la valeur de la case
        return self.cases[i][j]

    def setCase(self, i, j, val):
        # pour modifier la valeur de la case
        self.cases[i][j] = val

    def SymboleCase(self, val):
        #retourne le symbore correspondant à la valeur de la case
        if val == Mer or val == Bat:
            return "§"
        elif val == Tir:
            return "O"
        else:
            return "X"

    def initialiserG(self):
        for j in range(self.height):
            for i in range(self.width):
                self.cases[j][i] = 0

    def afficherG(self):
        for j in range(self.height):
            for i in range(self.width):
                print(self.SymboleCase(self.valCase(j, i)), end = "")
            print()

#class Navire():


G1 = Grille(3, 3)
G1.afficherG()





