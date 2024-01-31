#fichier introuvable
#fichier non lisible

fichier=input("Entrez le fichier à ouvrir :" )

try:
    f=open(fichier,"r")
    print(f.read())
except FileNotFoundError:
    print(f"Le fichier {fichier} est introuvable!")
except UnicodeDecodeError:
    print(f"Le Fichier {fichier} est impossible à ouvrir.")
else:
    f.close()

