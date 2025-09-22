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
import random

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
    [Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
    [Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, Case.CVide, ],
]

class caracteristiques:
    def __init__(self, color, char):
        self.char = char
        self.color = color

class LC:
    def __init__(self, l, c):
        self.l = l
        self.c = c

class Move:
    def __init__(self, from_position, to_position):
        self.from_position = from_position
        self.to_position = to_position

grilleColors = {
    Case.Doctor: caracteristiques(Back.BLUE, ' D '),
    Case.Dalek: caracteristiques(Back.RED, ' & '),
    Case.CVide: caracteristiques(Back.WHITE, ' _ ')
}

gotoxy(positionInitialX, positionInitialY)

for y, ligne in enumerate(grille):

    gotoxy(positionInitialX, positionInitialY + y)

    for case in ligne:
        objet = grilleColors[case]
        print(objet.color + objet.char, end='')

runGame = True
win = False
lose = False
niveau = 1

def lire_touche(m, arrow):
    if arrow == ArrowKeys.UP_LEFT:
        m.to_position.l -= 1
        m.to_position.c -= 1
    elif arrow == ArrowKeys.UP:
        m.to_position.l -= 1
    elif arrow == ArrowKeys.UP_RIGHT:
        m.to_position.l -= 1
        m.to_position.c += 1
    elif arrow == ArrowKeys.DOWN_LEFT:
        m.to_position.l += 1
        m.to_position.c -= 1
    elif arrow == ArrowKeys.DOWN:
        m.to_position.l += 1
    elif arrow == ArrowKeys.DOWN_RIGHT:
        m.to_position.l += 1
        m.to_position.c += 1
    elif arrow == ArrowKeys.LEFT:
        m.to_position.c -= 1
    elif arrow == ArrowKeys.RIGHT:
        m.to_position.c += 1

def move_doc(m, grille, positionInitialX, positionInitialY ):
    if (0 <= m.to_position.l < len(grille) and (0 <= m.to_position.c < len(grille[0])) and (grille[m.to_position.l][m.to_position.c] == Case.CVide)):
                    
        ## look for last position and Print new case bckGround
        gotoxy(positionInitialX + m.from_position.c * 3, positionInitialY + m.from_position.l)
        print(grilleColors[Case.CVide].color + grilleColors[Case.CVide].char, end='')

        ## Change grille value
        grille[m.from_position.l][m.from_position.c] = Case.CVide
        grille[m.to_position.l][m.to_position.c] = Case.Doctor

        ## Go to new position and print doc
        gotoxy(positionInitialX + m.to_position.c * 3, positionInitialY + m.to_position.l)
        print(grilleColors[Case.Doctor].color + grilleColors[Case.Doctor].char, end='')

        ## Last position == actual position
        m.from_position = LC(m.to_position.l, m.to_position.c)

while runGame:

    l = random.randint(0, len(grille) - 1)
    c = random.randint(0, len(grille[0]) - 1)

    grille[l][c] = Case.Doctor
    gotoxy(positionInitialX + c * 3, positionInitialY + l)
    print(grilleColors[Case.Doctor].color + grilleColors[Case.Doctor].char, end='')

    m = Move(LC(l, c),LC(l, c))

    dalekInGame = 3

    doctor_xy = [0,0]

    dalek_pos = [[0,0],[0,0],[0,0]]
    ## Dessin daleks 
    for i in range(dalekInGame * niveau):
        ##dalek_pos = [l_dalek , c_dalek]


        ## Give random position to the Dalek
        dalek_pos[i] = random.randint(0, len(grille) - 1)
        c_dalek[i] = random.randint(0, len(grille[0]) - 1)

        ## if the space in the Grille is empty print the fcking Dalek
        if grille[l_dalek][c_dalek] == Case.CVide:
            grille[l_dalek][c_dalek] = Case.Dalek
            gotoxy(positionInitialX + c_dalek * 3, positionInitialY + l_dalek)
            print(grilleColors[Case.Dalek].color + grilleColors[Case.Dalek].char, end='')
        ## else no sabemos todavia 


    def move_daleks():
        for _ in range(dalekInGame * niveau):
            ## look for last position and Print new case bckGround
            gotoxy(positionInitialX + m.from_position.c * 3, positionInitialY + m.from_position.l)
            print(grilleColors[Case.CVide].color + grilleColors[Case.CVide].char, end='')
             

    while not win and not lose:
        c = msvcrt.getch()
        m.to_position = LC(m.from_position.l, m.from_position.c)

        if c == b'\xe0':
            direction = msvcrt.getch()
            touche =ord(direction)

            try:
              arrow = ArrowKeys(touche)
            except ValueError:
                continue
            
            lire_touche(m,arrow)
            move_doc(m, grille, positionInitialX, positionInitialY)
            
            
        else:
            continue

