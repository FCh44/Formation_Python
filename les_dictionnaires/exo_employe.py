employes={
    "id01":{"prenom":"Paul","nom":"Dupont","age":35},
    "id02":{"prenom":"Julie","nom":"Dupuit","age":25},
    "id03":{"prenom":"Patrick","nom":"Ferrand","age":36},
}
del employes["id03"]
employes["id02"]["age"]=26
age_paul=employes.get("id01","id inconnu").get("age",0)
print(employes)
print(age_paul)