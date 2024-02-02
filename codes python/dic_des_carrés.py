def dic_des_carrés (n):
    resultat = {i:i*i for i in range(1, n+1)}
    return resultat

# saisie de la valeur entière de n 
while True:
    try:
        n = int(input("saisir la valeur de n(entier) :"))
        break
    except ValueError:
        print("veuillez saisir un entier valide.")


# Appeler la fonction dic_des_carrés et afficher le résultat

resultat_dic_des_carres = dic_des_carrés(n)
print(f"Dictionnaire des carrés jusqu'à {n} : {resultat_dic_des_carres}")
