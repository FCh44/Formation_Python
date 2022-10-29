import sys
LISTE_COURSE=[]
choix=""
MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
\U0001F449 Votre choix : """

MENU_CHOICE=["1","2","3","4","5"]


while (True):
    choix=input(MENU)
    print("\n")
    #Controles
    if choix not in MENU_CHOICE:
        print(f"\U000026D4 Votre choix doit être compris entre 1 et 5.")
        continue

    # 1- Ajout d'un element dans la liste
    if int(choix)==1:
        element=input("Entrez le nom de l'élement à ajouter à la liste de courses : ")
        # on teste si l"element est dejà present dans la liste
        if element.lower() in LISTE_COURSE:
            print(f"{element} est déja present dans la liste.")
        else:
            LISTE_COURSE.append(element.lower())
            print(f"L'élement {element} a bien été ajouté à la liste.")

    #2 -Retirer
    if int(choix)==2:
        element = input("Entrez le nom de l'élement à retirer de la liste de courses : ")
        # on teste si l"element est present dans la liste
        if element not in LISTE_COURSE:
            print(f"l'élement {element} n'est pas dans la liste de course.")
        else:
            LISTE_COURSE.remove(element.lower())
            print(f"l'élement {element} a été retiré de la liste de course.")

    #3-Affichage de la liste
    if int(choix)==3:
        print("Contenu de la liste de course")
        if not LISTE_COURSE:
            print("Votre liste de course est vide.")
        else:
            for i, element in enumerate(LISTE_COURSE,1):  #on commence avec un affichage d'indice à 1
                print(f"{i}. {element}")

   #4-Vider le liste
    if int(choix)==4:
        LISTE_COURSE.clear()
        print("La liste de course a été vidée.")

    #5-Quitter
    if int(choix)==5:
        print("A bientôt.")
        sys.exit()
    print("_" * 50)