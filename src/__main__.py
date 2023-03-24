from src.domena.igralec import Igralec
from src.domena.miza import Miza

stevilo_igralcev: int = int(input('Število igralcev: '))
miza = Miza()

for i in range(stevilo_igralcev):
    ime: str = input('Kako vam je ime: ')
    priimek: str = input('Vaš priimek: ')
    igralec: str = Igralec(ime=ime, priimek=priimek)
    miza.dodaj_igralca(igralec=igralec)

miza.razdeli_karte()

while not miza.konec_igre():
    miza.vrzite_karte()
    miza.preglej_vrzene_karte()
    for igralec in miza.igralci:
        print(f'{igralec.ime} {igralec.priimek}: tocke: {igralec.tocke()}')