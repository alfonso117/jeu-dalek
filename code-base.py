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

class Action(Enum):
    from enum import Enum
## aqui
class Action(Enum):
    UP_LEFT = 'G'
    UP = 'H'
    UP_RIGHT = 'I'
    LEFT = 'K'
    RIGHT = 'M'
    DOWN_LEFT = 'O'
    DOWN = 'P'
    DOWN_RIGHT = 'Q'
    TELETRANSPORTE = 't'
    ZAPPER = 'z'
## hasta aca
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
## aqui 
def lire_touche(m, touche):
    if touche == Action.UP_LEFT:
        m.to_position.l -= 1
        m.to_position.c -= 1
    elif touche == Action.UP:
        m.to_position.l -= 1
    elif touche == Action.UP_RIGHT:
        m.to_position.l -= 1
        m.to_position.c += 1
    elif touche == Action.DOWN_LEFT:
        m.to_position.l += 1
        m.to_position.c -= 1
    elif touche == Action.DOWN:
        m.to_position.l += 1
    elif touche == Action.DOWN_RIGHT:
        m.to_position.l += 1
        m.to_position.c += 1
    elif touche == Action.LEFT:
        m.to_position.c -= 1
    elif touche == Action.RIGHT:
        m.to_position.c += 1
    elif touche == Action.TELETRANSPORTE:
        m.to_position.l = random.randint(0, len(grille) - 1)
        m.to_position.c = random.randint(0, len(grille[0]) - 1)
## hasta aca


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
    ##for i in range(dalekInGame * niveau):
        ##dalek_pos = [l_dalek , c_dalek]


        ## Give random position to the Dalek
       ## dalek_pos[i] = random.randint(0, len(grille) - 1)
        ##c_dalek[i] = random.randint(0, len(grille[0]) - 1)

        ## if the space in the Grille is empty print the fcking Dalek
        ##if grille[l_dalek][c_dalek] == Case.CVide:
           ## grille[l_dalek][c_dalek] = Case.Dalek
            ##gotoxy(positionInitialX + c_dalek * 3, positionInitialY + l_dalek)
            ##print(grilleColors[Case.Dalek].color + grilleColors[Case.Dalek].char, end='')
        ## else no sabemos todavia 


    def move_daleks():
        for _ in range(dalekInGame * niveau):
            ## look for last position and Print new case bckGround
            gotoxy(positionInitialX + m.from_position.c * 3, positionInitialY + m.from_position.l)
            print(grilleColors[Case.CVide].color + grilleColors[Case.CVide].char, end='')
             
## aca
    while not win and not lose:
        touche = msvcrt.getch()
        m.to_position = LC(m.from_position.l, m.from_position.c)

        if touche == b'\xe0':
            touche = msvcrt.getch().decode("utf-8")
        else:
            touche = touche.decode("utf-8").lower()
            
        try:
            action = Action(touche)
            lire_touche(m, action)
            move_doc(m, grille, positionInitialX, positionInitialY)
        except ValueError:
            continue 
## hasta aqui

