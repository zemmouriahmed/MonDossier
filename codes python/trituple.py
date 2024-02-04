# saisie par l'utilisateur d'un tuple format (entier,flottant)

le_tuple =[]
while True:
    try:
        n = int(input("saisir le nombre d'éléments dans le tuple :"))
        break
    except ValueError:
        print("veuillez entrer un nombre entier valide")

for i in range(n):
    try:
        entier = int(input(f"entrer l'entier pour l'élément {i+1} :"))
        flottant = float(input(f"saisir le flottant pour l'élément {i+1}:"))
        le_tuple.append((entier, flottant))
    except ValueError:
        print("Veuiller entrer des valeurs valides.")

# tri du tuple par son élément flottant en utilisant une boucle while
        
i = 0
while i<len(le_tuple):
    j = i + 1
    while j < len(le_tuple):
        if le_tuple[i][1] > le_tuple[j][1]:

            # changer l'ordre des éléments si besoin
            le_tuple[i], le_tuple[j] = le_tuple[j], le_tuple[i]
        j += 1
    i += 1

# affichage du résultat
print(f"Tuple trié par son élément flottant : {le_tuple}")
