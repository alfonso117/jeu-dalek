# # Texte en couleur
# print(Fore.RED + "Ce texte est rouge")
# print(Fore.GREEN + "Ce texte est vert")
# print(Fore.BLUE + "Ce texte est bleu")

# # Fond coloré
# print(Back.YELLOW + "Fond jaune avec texte par défaut")

# # Style (gras, normal, etc.)
# print(Style.BRIGHT + "Texte en style BRIGHT")
# print(Style.RESET_ALL + "Retour au style normal")

import os
import time
from collections import defaultdict

from enum import Enum
from colorama import init, Fore, Back, Style
import msvcrt
import random

init(autoreset=True)

def gotoxy(x, y):
    print(f"\033[{y};{x}H", end='')

positionInitialX, positionInitialY = 15, 3

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

class Case(Enum):
    Doctor = 0
    Dalek = 1
    CVide = 2
    Cjunk = 3

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
        self.from_position:LC = from_position
        self.to_position:LC = to_position

grilleColors = {
    Case.Doctor: caracteristiques(Back.BLUE, ' D '),
    Case.Dalek: caracteristiques(Back.RED, ' & '),
    Case.CVide: caracteristiques(Back.WHITE, ' _ '),
    Case.Cjunk: caracteristiques(Back.YELLOW, ' X ')
}

## Print of the grill
for y, ligne in enumerate(grille):

    gotoxy(positionInitialX, positionInitialY + y)

    for case in ligne:
        objet = grilleColors[case]
        print(objet.color + objet.char, end='')

## Characters positions in the grille
doc_position = []
dalek_pos = []

## Read arrow key
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
       teletransporter(m)
    elif touche == Action.ZAPPER:
        zapp()


## Move doctor 
def move_doc(m:Move, grille, positionInitialX, positionInitialY ):
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
        doc_position = [m.from_position.l, m.from_position.c]

## get random Position
def random_position():
    ## Give random position to the Dalek
    x = random.randint(0, len(grille) - 1)
    y = random.randint(0, len(grille[0]) - 1)

    return x, y

def teletransporter(m:Move):
    m.to_position.l , m.to_position.c = random_position()
    move_doc(m, grille, positionInitialX, positionInitialY )
   

## Print one Dalek
def print_dalek(grille, l_dalek, c_dalek ):
        ## if the space in the Grille is empty print the fcking Dalek
        if grille[l_dalek][c_dalek] == Case.CVide:
            grille[l_dalek][c_dalek] = Case.Dalek
            ## GO and print new position
            gotoxy(positionInitialX + c_dalek * 3, positionInitialY + l_dalek)
            print(grilleColors[Case.Dalek].color + grilleColors[Case.Dalek].char, end='')
           
            ## Save 1 dalek position in the list of dalekssss
            dalek_pos.append([l_dalek, c_dalek]) 
        elif grille[l_dalek][c_dalek] == Case.Dalek:
            grille[l_dalek][c_dalek] = Case.Cjunk

            gotoxy(positionInitialX + c_dalek * 3, positionInitialY + l_dalek)
            print(grilleColors[Case.Cjunk].color + grilleColors[Case.Cjunk].char, end='')


## Print all daleks
def dessin_daleks(nbDaleks, niveau, grille):
        for i in range(nbDaleks + niveau):
            x, d = random_position()
            print_dalek(grille, x, d)


def if_lose():
    os.system('cls')
    print(Fore.RED + "YOU LOST!!! :(")
    time.sleep(3)

## Move daleks based in doc's position 
def move_daleks(dalek_pos, m:Move):
    global lose
    new_positions = []

    for i, (x, y) in enumerate(dalek_pos):
        if grille[x][y] != Case.Cjunk:
            gotoxy(positionInitialX + y * 3, positionInitialY + x)
            print(grilleColors[Case.CVide].color + grilleColors[Case.CVide].char, end='')
            grille[x][y] = Case.CVide

        # Mover en dirección al Doctor
        if x < m.to_position.l:
            x += 1
        elif x > m.to_position.l:
            x -= 1

        if y < m.to_position.c:
            y += 1
        elif y > m.to_position.c:
            y -= 1

        if x == m.to_position.l and y == m.to_position.c:
            if_lose()
            break


        new_positions.append((x, y))

    # Verificar colisiones y actualizar grilla
    dalek_pos.clear()
    positions_seen = {}

    for (x, y) in new_positions:
        if (x, y) in positions_seen:
            # Colisión → basura
            grille[x][y] = Case.Cjunk
            gotoxy(positionInitialX + y * 3, positionInitialY + x)
            print(grilleColors[Case.Cjunk].color + grilleColors[Case.Cjunk].char, end='')

        else:
            # Dalek válido
            positions_seen[(x, y)] = True
            grille[x][y] = Case.Dalek
            gotoxy(positionInitialX + y * 3, positionInitialY + x)
            print(grilleColors[Case.Dalek].color + grilleColors[Case.Dalek].char, end='')
            dalek_pos.append((x, y))

## Verify if the level is passed
def level_win():
    if len(dalek_pos) == 0:
        win = True
        niveau += 1
        os.system('cls') 
        print(Fore.GREEN + "You WON!!!!!")

        time.sleep(3)

def zapp():
    directions = [(-1,-1), (-1,0), (-1,1),
                  ( 0,-1),         ( 0,1),
                  ( 1,-1), ( 1,0), ( 1,1)]

    rows = len(grille)
    cols = len(grille[0])
    x, y = doc_position

    for direct_x, direct_y in directions:
        nx = x + direct_x
        ny = y + direct_y
        if 0 <= nx < rows and 0 <= ny < cols:
            if grille[nx][ny] == Case.Dalek:
                # Convertir en Junk en la grilla
                grille[nx][ny] = Case.Cjunk
                gotoxy(positionInitialX + ny * 3, positionInitialY + nx)
                print(grilleColors[Case.Cjunk].color + grilleColors[Case.Cjunk].char, end='')

                # Eliminar también de dalek_pos si está ahí
                if (nx, ny) in dalek_pos:
                    dalek_pos.remove((nx, ny))

gotoxy(positionInitialX, positionInitialY)
runGame = True
win = False
lose = False
niveau = 1
dalekInGame = 2

## Le jeu
while runGame:
    win = False
    lose = False
    ## Give the Doctor a random Position
    l = random.randint(0, len(grille) - 1)
    c = random.randint(0, len(grille[0]) - 1)
    ## Save his positon on the grille 
    grille[l -1][c -1 ] = Case.Doctor

    ## Print the Doctor (console) 
    gotoxy(positionInitialX + c * 3, positionInitialY + l)
    print(grilleColors[Case.Doctor].color + grilleColors[Case.Doctor].char, end='')

    ## Save his position in a new variable
    m = Move(LC(l-1, c-1),LC(l-1, c-1))
    doc_position = [m.from_position.l -1, m.from_position.c -1] ## Position [x,y] actuellement
    print(doc_position)
    dessin_daleks(dalekInGame, niveau, grille)              

    while not win and not lose:
        touche = msvcrt.getch()
        m.to_position = LC(m.from_position.l -1, m.from_position.c -1)

        if touche == b'\xe0':
            touche = msvcrt.getch().decode("utf-8")
        else:
            touche = touche.decode("utf-8").lower()
            
        try:
            action = Action(touche)
            lire_touche(m, action)
            move_doc(m, grille, positionInitialX, positionInitialY)
            move_daleks(dalek_pos, m)
            print(doc_position)
            
            level_win()

            
        except ValueError:
            continue 
