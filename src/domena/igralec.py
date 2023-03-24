from src.domena.karta import Karta


class Igralec:
    def __init__(self, ime: str, priimek: str):
        self.karte: list[Karta] = []
        self.ime: str = ime
        self.priimek: str = priimek

    def tocke(self) -> int:
        vsota = 0

        for karta in self.karte:
            vsota += karta.vrednost
        return vsota