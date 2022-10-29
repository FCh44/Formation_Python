for i in [0,2,8,45,1,6,1]:
    print(i)

for c in "Python":
    print(c)

for i in range(100):
    print("bonjour")

i=0
while i<10000:
    print("bonsoir")
    i+=1

#boucle for else

prenoms=["Pierre","Patrick","Marc","Jean"]
for prenom in prenoms:
    if prenom=="Patrick":
        print("Patrick a été trouvé!")
        break
else:
    print("Patrick est introuvable!")


for prenom in prenoms:
    if prenom=="Paul":
        print("Paul a été trouvé!")
        break
else:
    print("Paul est introuvable!")


#comprehensio de liste
nombres=[-5,-4,-3,-2,-1,0,1,2,3,4,5]

nombres_positifs=[i for i in nombres if i>0]
print(nombres_positifs)
print([i *2 for i in range(-5,6)])
print([i *2 for i in range(-5,6) if i<0])

notes=[12,20,10,18,13]
if any([x>18 for x in notes]):
    print("Au moins une personne a > 18!")
notes_c=[18,18,18,18,18]
if all([x==18 for x in notes_c]):
    print("toutes les personnes ont 18!")