from random import randint

VIE_JOUEUR_MAX=50
VIE_ENNEMI_MAX=50
RECUP_MIN=15
RECUP_MAX=50
NB_POTIONS=3
DEGAT_JOUEUR_MIN=5
DEGAT_JOUEUR_MAX=10
DEGAT_ENNEMI_MIN=5
DEGAT_ENNEMI_MAX=15


vie_joueur=VIE_JOUEUR_MAX
vie_ennemi=VIE_ENNEMI_MAX
potions=NB_POTIONS
potion_prise=False

while (vie_joueur>0 and vie_ennemi>0):
    if not potion_prise: # tour normal
        choix=input("Souhaitez vous attaquer ⚔(1) ou utiliser une potion 🧪(2) :")

        # controle
        if (choix != "1" and choix != "2"):
            continue

        # test attaque defense
        if choix == "1":
            attaque_joueur = randint(DEGAT_JOUEUR_MIN, DEGAT_JOUEUR_MAX)
            vie_ennemi -= attaque_joueur
            # Affichage des résultats du combat
            print(f"Vous avez infligé {attaque_joueur} points de dégats à l'ennemi.")

            if vie_ennemi > 0:
                attaque_ennemi = randint(DEGAT_ENNEMI_MIN, DEGAT_ENNEMI_MAX)
                vie_joueur -= attaque_ennemi
                # Affichage des résultats du combat
                print(f"L'ennemi vous a infligé {attaque_ennemi} points de dégats")

        if choix == "2":
            if potions > 0:
                recup_vie = randint(RECUP_MIN, RECUP_MAX)
                vie_joueur += recup_vie
                # on ne peut recuperer plus de vie que sa vie max
                if vie_joueur > VIE_JOUEUR_MAX:
                    vie_joueur = VIE_JOUEUR_MAX
                potions -= 1
                potion_prise = True
                print(f"Vous récupérez {recup_vie} points de vie")
            else:
                print("Dommage! Vous n'avez plus de potions.....")

            # l'ennemi attaque
            attaque_ennemi = randint(DEGAT_ENNEMI_MIN, DEGAT_ENNEMI_MAX)
            vie_joueur -= attaque_ennemi
            # Affichage des résultats du combat
            print(f"L'ennemi vous a infligé {attaque_ennemi} points de dégats")
    else: #seul l'ennemi attaque le jour passe sont tour
        #l'ennemi attaque
        attaque_ennemi = randint(DEGAT_ENNEMI_MIN, DEGAT_ENNEMI_MAX)
        vie_joueur -= attaque_ennemi
        potion_prise=False
        # Affichage des résultats du combat
        print(f"L'ennemi vous a infligé {attaque_ennemi} points de dégats")



    # Affichage
    print(f"Il vous reste {vie_joueur} points de vie.")
    print(f"Il vous reste {potions} potions 🧪.")
    print(f"Il reste {vie_ennemi} points de vie à l'ennemi.")
    print("_" * 50)

if vie_joueur>0 and vie_ennemi<=0:
    print("Vous avez gagné le combat!")
else:
    print("Vous êtes mort!")