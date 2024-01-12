
"""Fonction de recherche binaire dans une liste triée
Renvoie l'indice de l'élément s'il est présent, sinon
revoie -1."""
def recherche_binaire(liste, element):
    debut = 0
    fin =len(liste) - 1

    while debut <= fin:
        milieu = (debut + fin) // 2
        if liste[milieu] == element:
            return milieu
        elif liste[milieu] < element:
            debut = milieu + 1
        else:
            fin = milieu - 1

    return -1

# Fonction pour calculer la puissance d'un nombre
def puissance(a,b):
    return pow(a,b)

def tri_bulles(liste):
    """Effectue le tri à bulles sur une liste"""
    n = len(liste)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if liste [j] > liste[j+1]:
                #Echange les éléments
                temp = liste[j]
                liste[j] = liste[j+1]
                liste[j+1] = temp

def tri_fusion(liste):
    """Effectue le tri fusion sur une liste"""

    if len(liste) > 1:
        milieu = len(liste) // 2
        gauche = liste[:milieu]
        droite = liste[milieu:]

        tri_fusion(gauche)
        tri_fusion(droite)

        i = j = k = 0
        while i < len(gauche) and j < len(droite):
            if gauche[i] < droite[j]:
                liste[k] = gauche[i]
                i += 1

            else:
                liste[k] = droite[j]
                j += 1
            k += 1


        while i < len(gauche):
            liste[k] = gauche[i]
            i += 1
            k += 1

        while j < len(droite):
            liste[k] = droite[j]
            j += 1
            k += 1


def tri_rapide(liste):

    """Effectue le tri rapide sur une liste"""
    if len(liste) <= 1:
        return liste
    else:
        pivot = liste.pop()
        inferieur = []
        superieur = []
        for element in liste:
            if element <= pivot:
                inferieur.append(element)

            else:
                superieur.append(element)
# ensuite on procède à la concaténation des différentes listes
# sachant que l'élément [pivot] est une liste contenant uniquement
# l'élément pivot
        return tri_rapide(inferieur) + [pivot] + tri_rapide(superieur)



#PROGRAMME PRINCIPAL
    
if __name__ == "__main__":

    #Demander à l'utilisateur ce qu'il envisage de faire comme opération
    print("1. Recherche binaire\n2. Calcul de puissance\n3. Tri à bulles\n4. Tri Fusion\n5. Tri rapide")
    choix = int(input("Choisir le numéro de l'opération à effectuer : "))

    if choix == 1:
        #Recherche binaire
        liste = sorted([int(x) for x in input("Entrer une liste d'éléments triés séparés par des espaces :").split()])
        element = int(input("Entrer l'élément à rechercher :"))
        resultat = recherche_binaire(liste,element)
        if resultat != -1:
            print(f"L'élément {element} a été trouvé à l'indice {resultat}.")
        else:
            print(f"L'élément {element} n'a pas été trouvé dans la liste.")


    elif choix == 2:
        # calcul de puissance
        a = int(input("Entrer la valeur de 'a' : "))
        b = int(input("Entrer la valeur de 'b' : "))
        resultat = puissance(a,b)

        print(f"{a} à la puissance {b} est égal à {resultat}.")


    elif choix == 3:
        #Tri à bulles 
        liste = [int(x) for x in input("Entrer une liste d'éléments séparés par des espaces :").split()]
        tri_bulles(liste)
        print("Liste triée à l'aide du tri à bulles:",liste)



    elif choix == 4:
        #Tri fusion
        liste = [int(x) for x in input("Entrer la liste d'éléments séparés par un espace : ").split()]
        tri_fusion(liste)
        print("Liste triée à l'aide du tri fusion :",liste )


    elif choix == 5:
        #Tri rapide
        liste = [int(x) for x in input("Entrer la liste d'éléments séparés par un espace : ").split()]
        tri_rapide(liste)
        print("Liste triée à l'aide du tri rapide :",liste )