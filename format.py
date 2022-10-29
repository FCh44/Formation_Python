BONJOUR="Bonjour {prenom} {nom}."

prenom=input("Entrer votre prénom :\n")
nom=input("Entrer votre nom :\n")

print(BONJOUR.format(prenom=prenom,nom=nom))