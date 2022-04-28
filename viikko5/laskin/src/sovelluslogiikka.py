from copy import copy

class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = tulos

    def miinus(self, arvo):
        self.edellinen = copy(self.tulos)
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.edellinen = copy(self.tulos)
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.edellinen = copy(self.tulos)
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo
    
    def palauta_edellinen(self):
        #palaute = self.edellinen
        self.tulos = copy(self.edellinen)
