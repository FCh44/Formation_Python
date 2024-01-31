a=10
b=0

try:
    print(a/b)
except NameError:
    print("la valeur de b b'est pas défini.")
except ZeroDivisionError:
    print("Division par zero impossible")
else:
    print(b)
finally:
    print("Fin de bloc.")