liste_nom=["Maxime"]
print(liste_nom)
liste_nom.append("Jules")
liste_nom.append("Franck")
print(liste_nom)
liste_nom.extend(["Toto","Titi","TiTi"])
print(liste_nom)
liste_nom.remove("Titi") # ne retire que la 1er occurence trouvée
print(liste_nom)

employes=["Carlos","Max","Martine","Patrick","Alex","Max"]
employes_bis=["Carlos","Max","Martine","Patrick","Alex","Max"]
print(employes.index("Alex"))
print(employes.index("Max")) # index du premier rencontré dans la liste
print(employes.count("Max"))

employes.sort()   # tri la liste
employes.reverse() # inverse l'ordre de la liste
print(employes)

employes_trie=sorted(employes)
print(employes_trie)