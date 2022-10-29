while (True):
    nombre1 = input(">>>> Entrez un premier nombre :")
    nombre2 = input(">>>> Entrez un deuxieme nombre :")
    if ((not nombre1.isdigit()) or (not nombre2.isdigit())):
        print("Veuillez entrer deux nombre valides !")
        continue
    else:
        break
print(f"le résultat de l'addition de {nombre1} avec {nombre2} est égal à {int(nombre1)+int(nombre2)}.")