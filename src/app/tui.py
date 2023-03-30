from src.domena.igralec import Igralec
from src.domena.miza import Miza


class Tui:
    def __init__(self):
        self.miza: Miza = Miza()
        stevilo_igralcev: int = int(input('Število igralcev: '))
        for i in range(stevilo_igralcev):
            ime: str = input('Kako vam je ime: ')
            priimek: str = input('Vaš priimek: ')
            igralec: Igralec = Igralec(ime=ime, priimek=priimek)
            self.miza.dodaj_igralca(igralec=igralec)

        self.miza.razdeli_karte()

    def narisi(self):
        print(f'Trenutna runda: {self.miza.st_rund}')
        for igralec in self.miza.igralci:
            print(f'{igralec.ime} {igralec.priimek}: tocke: {igralec.tocke()}')

    def vnos(self):
        pass

    def naslednja_runda(self):
        self.miza.vrzite_karte()
        self.miza.preglej_vrzene_karte()

    def konec(self):
        return self.miza.konec_igre()
