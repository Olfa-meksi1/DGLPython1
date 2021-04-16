class Personne:
    def __init__(self, pname, plname):  ## constructeur avec des attributs
        self.name = pname
        self.lname = plname

    def SePresenter(self):               ## Méthode se présenter
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


P1 = Personne("Olfa", "Meksi")
P1.SePresenter()
P1.set_name("Amel")
P1.SePresenter()