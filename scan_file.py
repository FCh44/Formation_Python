from pathlib import Path

#recupération des dossier et fichier d'un répetoire
for f in Path.home().iterdir():
    print(f.name)


directories=[ f.name for f in Path.home().iterdir() if  f.is_dir()]
print(directories)

files=[ f.name for f in Path.home().iterdir() if  f.is_file()]
print(files)


# avec le module glob
p=Path.home()/"Downloads"

for f in p.glob("*.JPG"):
    print(f.name)

#en mode recursif
for f in p.rglob("*.JPG"):
    print(f.name)