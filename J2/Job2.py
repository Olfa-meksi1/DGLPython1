class Personne:
    def __init__(self, pname, plname):  ## constructeur avec des attributs
        self.name = pname
        self.lname = plname

    def SePresenter(self):  ## Méthode se présenter
        print("my name is: ", self.name, self.lname)

    def get_name(self):
        print("enter the name: ")
        return self.name

    def get_lname(self):
        print("enter the name: ")
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def set_lname(self, new_lname):
        self.lname = new_lname

class Auteur(Personne):
    def __init__(self, Aname, Alname):
        super().__init__(Aname, Alname)
        self.oeuvre = []     # Colection des livres
    def listerOeuvre(self):
        str = '-'.join(self.oeuvre)
        print("The list of books of this auther is:", str)
    def ecrireUnLivre(self, titre):
        L1 = Livre(titre)
        self.oeuvre.append(titre)

class Livre:
    def __init__(self, titre):
        self.titre = titre
        self.auteur = Auteur
    def print_livre(self):
        print("The title of the book is: ", self.titre)

A1 = Auteur("François", "Gimeno")
A1.SePresenter()
A1.listerOeuvre()

A1.ecrireUnLivre("D")
A1.listerOeuvre()

A2 = Auteur("Olfa", "Meksi")
A2.SePresenter()
A2.listerOeuvre()

A2.ecrireUnLivre("E")
A2.listerOeuvre()
