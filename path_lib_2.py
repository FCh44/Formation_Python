from pathlib import Path

p=Path.cwd()
print(p)
p=p/"file_in"/"dossier"/"test"/"text.txt"
print(p.parent/p.stem)
print(p.parent/(p.stem+"-lowres"+p.suffix))
p.rename(p.parent/(p.stem+"-lowres"+p.suffix))
