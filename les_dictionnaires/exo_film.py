films={
    "Le Seigneur des Anneaux":12,
    "Harry Potter":9,
    "Blade Runner":7.5
}
prix=0

for key in films:
    prix+=films.get(key,0)
    #ou prix+=films[key]

print(f"Prix total {prix}")
