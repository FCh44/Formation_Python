for i in range(1,11):
    print(f"Utilisateur {i}")

i=len("Python")-1
while i>=0:
    print("Python"[i])
    i-=1

for lettre in reversed('Python'):
    print(lettre)

mot="Bonjour"

for lettre in mot[::-1]:
    print(lettre)

mot = "Python"

for i in range(len(mot)):
    print(i)
nombre=7
for i in range(11):
    print(f"{i} x {nombre} = {i*nombre}")