import os
import json
chemin="file_in/dossier/test/text.txt"
dir_in="file_in/dossier/test"
dir_out="file_out/dossier/test"

if not os.path.exists(dir_out):
    os.makedirs(dir_out)


#Lecture de fichiers
f=open(os.path.join(dir_in,"text.txt"),"r",encoding="utf-8")
print(f)
f.close()

#syntaxe sans le f.close
with open(os.path.join(dir_in,"text.txt"),"r",encoding="utf-8") as f:
   contenu=f.read()
   print(contenu)
print()
with open(os.path.join(dir_in,"text.txt"),"r",encoding="utf-8") as f:
   contenu=f.readlines()
   print(contenu)
print("Sans le \\n")
with open(os.path.join(dir_in,"text.txt"),"r",encoding="utf-8") as f:
   contenu=f.read().splitlines()
   print(contenu)

#ecriture de fichiers
with open(os.path.join(dir_out,"text_out.txt"),"w",encoding="utf-8") as f:
    f.write("Mode de fonctionnement.\n")

with open(os.path.join(dir_out,"text_out.txt"),"a",encoding="utf-8") as f:
    f.write("etape.\n")


#Les fichiers JSON
json_file="test.json"
with open(os.path.join(dir_out,json_file),"w",encoding="utf-8") as f:
    json.dump(list(range(10)),f)

with open(os.path.join(dir_in,json_file),"r",encoding="utf-8") as f:
    data=json.load(f)

print(data)
#on recupère la liste de la clé "liste"
donnee=data["liste"]

#modification des donnee dans le fichier json
donnee.append(10)
with open(os.path.join(dir_in,json_file),"w",encoding="utf-8") as f:
    json.dump({"liste":donnee,"couleur":"rouge","taille":22},f,indent=4)