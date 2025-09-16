from colorama import init, Fore, Back, Style

# Initialisation (nécessaire sur Windows)
init()

# # Texte en couleur
# print(Fore.RED + "Ce texte est rouge")
# print(Fore.GREEN + "Ce texte est vert")
# print(Fore.BLUE + "Ce texte est bleu")

# # Fond coloré
# print(Back.YELLOW + "Fond jaune avec texte par défaut")

# # Style (gras, normal, etc.)
# print(Style.BRIGHT + "Texte en style BRIGHT")
# print(Style.RESET_ALL + "Retour au style normal")

def gotoxy(x, y):
    print(f"\033[{y};{x}H", end='')

for i in range (27):
    print(Back.WHITE + "_" * 80)

print(Style.RESET_ALL)

