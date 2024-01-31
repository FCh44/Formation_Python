from pathlib import Path

BASE_DIR="C:\\Users\\fchar\Documents\\PythonProjects\\TestProjects"

file_prenom=Path(BASE_DIR)/"prenoms.txt"
file_prenom_ordered=Path(BASE_DIR)/"prenoms_order.txt"

#lecture du fichier
with file_prenom.open(encoding='utf-8',newline='\n') as f:
    lines=f.read().splitlines()

#Creation et alimentation de la liste des prenoms
prenoms=[]
for line in lines:
    prenoms.extend(line.split())
print(prenoms)

#nettoyage des carateres spéciaux
prenoms=[p.strip(',. ') for p in prenoms]

#tri de la liste
prenoms_sorted=sorted(prenoms)
print(prenoms_sorted)

#ecriture du fichier de sortie
with file_prenom_ordered.open("w",encoding='utf-8') as f:
    f.write("\n".join(prenoms_sorted))