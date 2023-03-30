import sys

from src.domena.igralec import Igralec
from src.domena.miza import Miza
import pygame


class Gui:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.miza: Miza = Miza()
        stevilo_igralcev: int = int(input('Število igralcev: '))
        for i in range(stevilo_igralcev):
            ime: str = input('Kako vam je ime: ')
            priimek: str = input('Vaš priimek: ')
            igralec: Igralec = Igralec(ime=ime, priimek=priimek)
            self.miza.dodaj_igralca(igralec=igralec)

        self.miza.razdeli_karte()

    def narisi(self):
        self.screen.fill("purple")
        pygame.draw.rect(self.screen, "red", (100, 100, 200, 200))
        pygame.display.flip()
        input('Dan: ')

    def vnos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def naslednja_runda(self):
        self.miza.vrzite_karte()
        self.miza.preglej_vrzene_karte()

    def konec(self):
        return self.miza.konec_igre()
