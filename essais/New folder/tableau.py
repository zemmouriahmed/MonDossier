import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import QRect, Qt
from case_spe import initialiser_cases_speciales
from affichage import AffichagePlateau


class Plateau:
    def __init__(self):
        self.taille_case = 40  # Cell size

        # Initialisez 'plateau' comme une grille vide
        self.plateau = [[None for _ in range(15)] for _ in range(16)]

        # Initialisation et stockage des cases spéciales
        self.cases_speciales = initialiser_cases_speciales()


    def placer_tuiles(self, tuiles):
        for tuile in tuiles:
                self.mettre_tuile(tuile, tuile.x, tuile.y)

    def est_case_occupee(self, x, y):
        # Check if the position is within the restricted area
        if y == 15 and x >= 7:  # Adjusting indices for zero-based grid
            return True
        return self.plateau[y][x] is not None

    def mettre_tuile(self, tuile, x, y):
        # Assurez-vous que l'indexation est correcte et que la case n'est pas déjà occupée
        if not (0 <= x < 15 and 0 <= y < 16) or self.plateau[y][x] is not None:
            raise ValueError("Position invalide ou déjà occupée.")
        self.plateau[y][x] = tuile

    # Ajoutez cette méthode à votre classe Plateau pour gérer le déplacement :

    def déplacer_tuile(self, tuile, position_originale, nouvelle_position):
        x_orig, y_orig = position_originale
        x_nouv, y_nouv = nouvelle_position
        # Assurez-vous de nettoyer l'ancienne position.
        self.plateau[y_orig][x_orig] = None
        # Mettre à jour la position de la tuile.
        tuile.x, tuile.y = x_nouv, y_nouv
        self.plateau[y_nouv][x_nouv] = tuile

# Fonction pour lancer l'application
# tableau.py
# tableau.py

def run(cases_speciales, plateau, taille_case):
    fenetre = AffichagePlateau(cases_speciales, plateau, taille_case)
    fenetre.show()
    return fenetre

if __name__ == '__main__':
    run()
