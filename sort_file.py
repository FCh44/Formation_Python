from pathlib import Path

dirs={".png" :"Pictures",
    ".jpg":"Pictures",
    ".jpeg":"Pictures",
    ".pdf":"Documents/pdf",
    ".txt":"Documents/txt",
    ".mp3":"Music"
}

tri_dir=Path.home()/"Downloads"

files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files:
    output_dir=tri_dir/dirs.get(f.suffix,"Autres")
    output_dir.mkdir(parents=True,exist_ok=True)  #creation reperetoire et sous repertoire (parent=True)
    f.rename(output_dir/f.name)