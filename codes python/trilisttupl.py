def trier_par_dernier_element(liste_de_tuples):

    liste_de_tuples.sort(key=lambda x:x[-1])
    liste_tuples_str = input("entrer une liste de tuples (séparer les éléments par des virgules et les tuples par des point virgules ):")
    liste_tuples=[tuple(map(int,tuple_str.split(','))) for tuple_str in liste_de_tuples.split(';')]
    trier_par_dernier_element(liste_tuples)
    print(f"liste des tuples triée par ordre croissant des derniers éléments: {liste_tuples}")