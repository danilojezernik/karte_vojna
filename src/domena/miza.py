from src.domena.igralec import Igralec
from src.domena.karta import Karta


class Miza:
    def __init__(self):
        self.karte: list[Karta] = []
        self.igralci: list[Igralec] = []