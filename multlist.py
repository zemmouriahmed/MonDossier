liste_str = input("Entrer la liste d'entiers séparés par des espaces:")
ma_liste = [int(element) for element in liste_str.split()]
resultat_multiplication = 1
resultat_intermediaire = []
for element in ma_liste :
    resultat_multiplication *= element
    resultat_intermediaire.append(str(resultat_multiplication))
    derniere_valeur = int(resultat_intermediaire[-1])

    print(f"le résultat de la multiplication des éléments de la liste {ma_liste} est :{derniere_valeur}")