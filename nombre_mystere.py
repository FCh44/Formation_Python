import random
#nombre d'essai
ESSAIS = 5
#borne min
MIN = 0
#borne max
MAX = 100
#generation d'un nombre aléatoire entre MIN et MAX
nombre_mystere = random.randint(MIN,MAX)

print("--- Le nombre_mystere ---\n")

nombre_essai = 0

while (nombre_essai < ESSAIS):
    print(f"Il vous reste {ESSAIS - nombre_essai} essai{'s' if (ESSAIS - nombre_essai) >1 else ''}.")
    nombre = input(f"Entrez un nombre entre {MIN} et {MAX} : ")
    if ((not nombre.isdigit()) or int(nombre) < MIN or int(nombre) > MAX):
        print("Entrez un nombre valide.")
        continue
    if int(nombre)<nombre_mystere:
        print(f"le nombre mystere est plus grand que {nombre}.\n")
        nombre_essai += 1
    elif int(nombre)>nombre_mystere:
        print(f"le nombre mystere est plus petit que {nombre}.\n")
        nombre_essai += 1
    else:
        print(f"GAGNE! Le nombre mystère est bien {nombre_mystere}")
        break
if nombre_essai == ESSAIS:
    print(f"PERDU! le nombre mystère était {nombre_mystere}")
print("Fin du jeu.")





