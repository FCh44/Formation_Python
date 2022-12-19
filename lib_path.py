from pathlib import Path
import shutil
#chemin utilisateur
print(Path.home())
#dossier courant
print(Path.cwd())

p=Path.cwd()

file = p.joinpath("file_in","dossier","test","test.json")

print(file.name)
print(file.parent)
print(file.stem)
print(file.suffix)
print(file.suffixes)
print(file.parts)
print(file.exists())
print(file.is_dir())
print(file.is_file())

p=p/"file_in"/"dossier_fc"
p.mkdir(exist_ok=True)
p=p/"1"/"2"/"3"
p.mkdir(parents=True,exist_ok=True)
p=p/"readme.txt"
#creation du fichier
p.touch()
#suppression du fichier
p.unlink()
p=p.parent
p.rmdir()
p=p.parent.parent.parent
print(p)
#on utilise shutile pour suppriler des dossiers non vide
shutil.rmtree(p)