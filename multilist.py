def multiplier_list(liste):
    produit = 1
    for element in liste:
        produit *= element
    return produit

# entrée des données
liste_entrée = input("entrer les éléments de la liste séparés par des espaces :").split()

# convertir les éléments de la liste en entiers
la_liste = [int(element) for element in liste_entrée]

# éxécution du code
résultat_multiplication = multiplier_list(la_liste)

print(f"Le résultat de la multiplication des éléments de la liste est: {résultat_multiplication}")