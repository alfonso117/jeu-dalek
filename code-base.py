# # Texte en couleur
# print(Fore.RED + "Ce texte est rouge")
# print(Fore.GREEN + "Ce texte est vert")
# print(Fore.BLUE + "Ce texte est bleu")

# # Fond coloré
# print(Back.YELLOW + "Fond jaune avec texte par défaut")

# # Style (gras, normal, etc.)
# print(Style.BRIGHT + "Texte en style BRIGHT")
# print(Style.RESET_ALL + "Retour au style normal")

from enum import Enum
from colorama import init, Fore, Back, Style
import msvcrt

init(autoreset=True)

def gotoxy(x, y):
    print(f"\033[{y};{x}H", end='')

positionInitialX, positionInitialY = 15, 3

class ArrowKeys(Enum):
    UP_LEFT = 71
    UP = 72
    UP_RIGHT = 73
    LEFT = 75
    RIGHT = 77
    DOWN_LEFT = 79
    DOWN = 80
    DOWN_RIGHT = 81

class Case(Enum):
    Doctor = 0
    Dalek = 1
    CVide = 2

grille = [
    [Case.Doctor, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.Dalek, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.Dalek, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.Dalek, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.Dalek, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.Dalek, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.Dalek, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.Dalek, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.Dalek, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.Dalek, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.Dalek, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.Dalek, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.Dalek, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.Dalek, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.Dalek, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.Dalek, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
]

class caracteristiques:
    def __init__(self, color, char):
        self.char = char
        self.color = color

grilleColors = {
    Case.Doctor: caracteristiques(Back.BLUE, 'D '),
    Case.Dalek: caracteristiques(Back.RED, '& '),
    Case.CVide: caracteristiques(Back.WHITE, ' _ ')
}

gotoxy(positionInitialX, positionInitialY)

for y, ligne in enumerate(grille):

    gotoxy(positionInitialX, positionInitialY + y)

    for case in ligne:
        objet = grilleColors[case]
        print(objet.color + objet.char, end='')

msvcrt.getch()
