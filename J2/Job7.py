class Personne:
    def __init__(self, pname, plname):  ## constructeur avec des attributs
        self.name = pname
        self.lname = plname

    def SePresenter(self):  ## Méthode se présenter
        return self.name+ " " + self.lname

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

class Livre:
    def __init__(self, titre):
        self.titre = titre
        self.auteur = Auteur
    def print_livre(self):
        print("The title of the book is: ", self.titre)

class Auteur(Personne):
    def __init__(self, Aname, Alname):
        super().__init__(Aname, Alname)
        self.oeuvre = []  # Liste pour la colection des livres

    def listerOeuvre(self):
        str = '-'.join(self.oeuvre)
        print(" **** Liste of books of", self.SePresenter()," is :", str)

    def ecrireUnLivre(self, titre):
        L1 = Livre(titre)
        self.oeuvre.append(titre)

class Client(Personne):
    def __init__(self, Cname, Clname, collection):
        super().__init__(Cname, Clname)
        self.collection = []  # liste qui contient les titres des livres

    def inventaire(self):
            print(self.collection)

class Bibliotheque:
    def __init__(self, nom, catalogue):  ## constructeur avec des attributs
        self.nom = nom
        self.catalogue = {}  #dictionnaire
    def acheterLivre(self, Auteur, titre,Q):
        existe = True
        for cle, val in self.catalogue.items():
            if titre == cle:
                print("Le livre", cle, "existe")
                self.catalogue[cle] = self.catalogue[cle] + Q
            else:
                existe = False

        if not existe or len(self.catalogue) == 0 :
            self.catalogue[titre] = Q

    def inventaire(self):
        for cle, val in self.catalogue.items():
            print("Il existe ", val, "copies du livre ", cle)

    def louer(self, Client, titre):
        exist = True
        for cle, val in self.catalogue.items():
            if titre == cle and val!= 0:
                # ajouter à la collection du client
                Client.collection.append(cle)
                #mettre à jour val = val -1
                self.catalogue[titre] = val -1
            else:
                exist = False
        if not exist or len(self.catalogue) == 0:
            print("Ce livre n'est pas en stock pour le moment")

    def rendreLivres(self, Client):
        for cle, val in self.catalogue.items():
            for k in range(len(Client.collection)):
                if cle == Client.collection[k]:
                    #print("Le livre", cle, "existe")
                    self.catalogue[cle] = self.catalogue[cle] + 1
                    Client.collection.remove(Client.collection[k])
                    k = k+1


A1 = Auteur("François", "Gimeno")
A1.ecrireUnLivre("AG")
A1.ecrireUnLivre("BG")
A1.listerOeuvre()

A2 = Auteur("Olfa", "Meksi")
A2.ecrireUnLivre("AM")
A2.listerOeuvre()


B1 = Bibliotheque("B1", "C1")
B1.acheterLivre("Olfa", "AM", 4)
B1.acheterLivre("Olfa", "BM", 2)
B1.acheterLivre("Olfa", "BM", 2)
B1.inventaire()

C1 = Client("Hugo", "Toto", "")
C1.inventaire()
B1.louer(C1, "AM")
C1.inventaire()
B1.inventaire()

B1.louer(C1, "DM")

B1.rendreLivres(C1)
B1.inventaire()
C1.inventaire()

