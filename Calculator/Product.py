
class Product():

    def __init__(self, name, protein, carbonates, fats, energy):
        self.__name = name
        self.__protein = protein
        self.__carbonates = carbonates
        self.__fats = fats
        self.__energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def protein(self):
        return self.__protein

    @protein.setter
    def protein(self, protein):
        self.__protein = protein


    @property
    def carbonates(self):
        return self.__carbonates

    @carbonates.setter
    def carbonates(self, carbonates):
        self.__carbonates = carbonates


    @property
    def fats(self):
        return self.__fats

    @fats.setter
    def fats(self, fats):
        self.__fats = fats


    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, energy):
        self.__energy = energy


