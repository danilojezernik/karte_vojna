import random

from src.domena.igralec import Igralec
from src.domena.karta import Karta, Znak


class Miza:
    def __init__(self):
        self.karte: list[Karta] = []
        self.igralci: list[Igralec] = []

    def dodaj_igralca(self, igralec: Igralec):
        self.igralci.append(igralec)

    def razdeli_karte(self):
        st_igralci = len(self.igralci)
        karte = []
        for i in range(2, 15):
            for znak in Znak:
                karta = Karta(vrednost=i, znak=znak)
                karte.append(karta)
        random.shuffle(karte)
        for i, karta in enumerate(karte):
            igralec = self.igralci[i % st_igralci]
            igralec.dodaj_karto(karta)
        self.igralci[-1].dodaj_karto(karte[-1])

