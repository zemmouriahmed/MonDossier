import Numpy as np 

# Demander à l'utilisateur de saisir le nombre d'élèves et le nombre de matières
nombre_eleves = int(input("Entrer le nombre d'élèves :"))
nombre_matieres = int(input("Entrer le nombre de matières :"))

#Creer un tableau numpy pour stocker les notes de chaque eleve dans chaque matiere
notes = np.zeros((nombre_eleves, nombre_matieres))

#Demander à l'utilisateur de saisir les notes de chaque elevepour chaque matiere
for i in range(nombre_eleves):
    print(f"\nSaisie des notes pour l'élève {i+1}:")
    for j in range(nombre_matieres):
        notes[i][j] = float(input(f"Note pour la matière{j+1}:"))

#Calculer la note totale pour chaque élève en utilisant la fonction sum() de numpy
notes_totales = np.sum(notes, axis=1)

#Calculer le pourcentage pour chaque élève
pourcentages = (notes_totales/nombre_matieres)

#Determiner la note finale pour chaque eleve en utilisant le systeme de notation
notes_finales = np.where(pourcentages >= 90, 'A+' ,
                         np.where(pourcentages >= 80, 'A',
                                 np.where(pourcentages >= 70, 'B+',
                                        np.where(pourcentages >= 60, 'B',
                                                 np.where(pourcentages >= 50, 'C', 'F')) )))

#Afficher le résultat sous forme de tableau
print("\nRésultats pour chaque élève : ")
print("{:<15} {:<12} {:<15} {:<12}" .format("Nom de l'élève" , "Note totale" , "Pourcentage" , "Note Finale"))
for i in range(nombre_eleves):
    print("{:<15} {:<12} {:<15} {:<12}" .format(f"Elève {i+1}" , notes_totales[i] , round(pourcentages[i], 2), notes_finales[i]))