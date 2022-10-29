import random

r=random.randint(0,1) # nombre entier entre 0 et 1 inclu
print(r)

r=random.uniform(0,1) # nombre float entre 0 et 1 inclu
print(r)

r=random.randrange(2) # nombre entier entre 0 et 2 exclu
print(r)


r=random.randrange(0,101,10) # nombre entier entre 0 et 101 exclu avec un pas de 10
print(r)

a=random.randrange(11)
b=random.randrange(11)

if a>b:
    print("Le nombre a est plus grand que le nombre b.")
elif a<b:
    print("Le nombre b est plus grand que le nombre a.")
else:
    print("Le nombre a et le nombre b sont égaux.")