#nombre=int(input("Entrer un nombre "))
#print(nombre)
print("1, 21, 3, 6".split(', '))
list=['1','2','2','4']
print("+".join(list))
print("9".zfill(4))

for i in range(11):
    print(str(i).zfill(2))

print("recherche d'une chaine de caractère")
print("Bonjour le jour".find("jour"))
print("Bonjour le jour".find("soir"))
print("Bonjour le jour".rfind("jour"))
print("\n")
print("recherche si une chaine de caractere se termine par") 
print("image.png".endswith(".png"))
print("recherche si une chaine de caractere commence par") 
print("image.png".startswith("im"))
"""nombre=input("Entrer un nombre ")
if nombre.isdigit():
    nombre=int(nombre)
else:
    print("Nombre non numérique!")"""

phrase="Bonjour le monde"
nouvelle_phrase=phrase.replace("jour","soir")
print(nouvelle_phrase)
print("\n")
chaine="Pierre, Julien, Anne, Marie, Lucien"
chaine_l=chaine.split(", ")
chaine_l.sort()
chaine_en_ordre=", ".join(chaine_l)
