import sys
note = 18
commentaire = ""



if note==20:
    commentaire = "C'est un sans faute !"
elif note >= 18:
    commentaire = "Excellent !!"
elif note > 14:
    commentaire = "Bon travail !"
elif note > 10 :
    commentaire = "Peut mieux faire."
elif note > 6 :
    commentaire = "Il faut tout revoir..."
elif note >= 3:
    commentaire = "Tu n'as rien compris !"
else:
    commentaire = "Sans commentaire..."

print(commentaire)