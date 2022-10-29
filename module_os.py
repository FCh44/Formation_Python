import os

chemin="Formation_Udemy/file_in"
dossier_test=os.path.join(chemin,"dossier","test2")
print(dossier_test)
#creation des répertoires
if not os.path.exists(dossier_test):
    os.makedirs(dossier_test)

#ou
#os.makedirs(dossier_test,exist_ok=True)

#suppression des repertoire
if os.path.exists(dossier_test):
    os.removedirs(dossier_test)