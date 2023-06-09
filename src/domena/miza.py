import random

from src.domena.igralec import Igralec
from src.domena.karta import Karta, Znak


class Miza:
    def __init__(self):
        self.vrzene_karte: list[Karta] = []
        self.igralci: list[Igralec] = []
        self.st_rund: int = 0

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

        i = 0
        for karta in karte:
            igralec = self.igralci[i]
            igralec.karte.append(karta)
            i += 1
            if i >= st_igralci:
                i = 0

    def vrzite_karte(self):
        for igralec in self.igralci:
            dobljena_karta = igralec.karte.pop(0)
            self.vrzene_karte.append(dobljena_karta)

    def preglej_vrzene_karte(self):
        max_karta = self.vrzene_karte[0]
        max_index = 0
        mesto = 0
        for karta in self.vrzene_karte:
            if karta.vrednost > max_karta.vrednost:
                max_index = mesto
                max_karta = karta
            mesto += 1

        zmagovalec = self.igralci[max_index]

        self.vrzene_karte.pop(0)

        zmagovalec.karte += self.vrzene_karte
        self.vrzene_karte = []

        self.st_rund += 1

    def konec_igre(self) -> bool:
        stevec = 0
        kos = []
        for igralec in self.igralci:
            if igralec.tocke() > 0:
                stevec += 1
            else:
                kos.append(igralec)

        for igralec in kos:
            self.igralci.remove(igralec)

        if stevec == 1:
            return True
        else:
            return False
