

from pathlib import Path


BASE_DIR="C:\\Users\\fchar\Documents\\PythonProjects\\TestProjects"


d={
    "Films":["Le_seigneur_des_anneaux",
             "Harry_Potter",
             "Moon",
             "Forrest_Gump"],
    "Employes":["Paul",
                "Pierre",
                "Marie"],
    "Exercices":["les_variables",
                 "les_fichiers",
                 "les_boucles"]
}


for dossier_principal,sous_dossier in d.items():
    for dossier in sous_dossier:
        chemin_dossier=Path(BASE_DIR)/dossier_principal/dossier
        print(dossier)
        chemin_dossier.mkdir(exist_ok=True,parents=True)