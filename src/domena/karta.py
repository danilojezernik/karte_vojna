from enum import Enum


class Znak(Enum):
    SRCE = 'SRCE'
    PIK = 'PIK'
    KARA = 'KARA'
    KRIZ = 'KRIZ'


class Karta:
    def __init__(self, vrednost: int, znak: Znak):
        self.vrednost: int = vrednost
        self.znak: Znak = znak

    def __str__(self):
        return f'Karta: {self.vrednost} - Znak {self.znak}'