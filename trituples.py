def tri_tuples (liste_de_tuples): 

    # filtrer les tuples non vides 
    tuples_non_vides = [tup for tup in liste_de_tuples if len(tup) > 0]

    # tri des tuples en utlisant sort

    tuples_non_vides.sort (key=lambda x: x[-1])
    return tuples_non_vides

# input utlisateuur de liste de tuples 
liste_entrée = input("entrer les tuples séparés par des virgules (par exemple, (1,2,3),(4,5,6)):")

# utilisation de la fonction eval() pour transformer cette chaîne en liste de tuples
la_liste = eval(liste_entrée)

# utilisation de la fonction de tri des tuples et résultat affichage
resultat_tri = tri_tuples (la_liste)

print(f"liste triée : {resultat_tri}")