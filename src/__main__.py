from src.domena.igralec import Igralec
from src.domena.karta import Karta, Znak
from src.domena.miza import Miza

miza = Miza()
igralec = Igralec("Danilo", "Jezernik")
miza.dodaj_igralca(igralec)
miza.razdeli_karte()
