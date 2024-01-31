from pathlib import Path


EXTENSIONS_MAPPING ={
    "mp3":"Musique",
    "wav":"Musique",
    "flac":"Musique",
    "avi":"Videos",
    "mp4":"Videos",
    "gif":"Videos",
    "bmp":"Images",
    "png":"Images",
    "jpg":"Images",
    "txt":"Documents",
    "pptx":"Documents",
    "csv":"Documents",
    "xls":"Documents",
    "odp":"Documents",
    "pages":"Documents",
    "pdf":"Documents",
}
#scan directory
BASE_DIR=Path.home()/'Downloads'
dir_data=BASE_DIR/'sources/data'

#list file in scan directory.

files_list=[f for f in dir_data.iterdir() if f.is_file()]
print(files_list)

#clasement des fichiers

for f in files_list:
    #print(f.suffix)
    #repertoire de destination
    dir_dest=BASE_DIR/EXTENSIONS_MAPPING.get(f.suffix[1:],"Divers")
    #print(dir_dest)
    dir_dest.mkdir(exist_ok=True)
    #déplacement vers le répertoire de destination
    f.rename(dir_dest/(f.name))
