import sys
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QLabel
from PyQt5.QtGui import QPainter, QColor, QFont

class Damier(QMainWindow):
    def __init__(self):
        super().__init__()
        # Configure la fenêtre principale
        self.setWindowTitle('Damier 15x15 avec tuiles rouges numérotées - PyQt5')  # Titre de la fenêtre
        self.setGeometry(100, 100, 600, 600)  # Position et dimensions de la fenêtre (x, y, largeur, hauteur)
        # Couleurs utilisées dans l'application
        self.couleur1 = QColor(0, 0, 0)  # Couleur noire pour une case du damier
        self.couleur2 = QColor(255, 255, 255)  # Couleur blanche pour l'autre case du damier
        self.couleurTuile = QColor(255, 0, 0)  # Couleur rouge pour les tuiles
        self.taille_case = 40  # Taille d'une case du damier
        self.agrandissement = 1.1  # Facteur d'agrandissement des tuiles lors de la sélection
        # Dictionnaire pour stocker la position initiale des tuiles numérotées de 1 à 7
        self.tuiles = {i: (i-1, 0) for i in range(1, 8)}
        self.tuileSelectionnee = None  # Stocke la tuile actuellement sélectionnée
        self.taille_tuile = self.taille_case  # Taille initiale d'une tuile
        self.positionOriginale = None  # Pour stocker la position originale d'une tuile sélectionnée

    def mousePressEvent(self, event):
        # Gère les événements de pression de la souris
        x, y = event.x() // self.taille_case, event.y() // self.taille_case
        for numero, position in self.tuiles.items():
            if (x, y) == position:
                self.tuileSelectionnee = numero
                self.positionOriginale = position  # Sauvegarde la position originale de la tuile
                self.taille_tuile = int(self.taille_case * self.agrandissement)  # Agrandit la tuile
                self.update()  # Met à jour l'affichage
                break

    def mouseMoveEvent(self, event):
        # Permet de déplacer la tuile sélectionnée avec la souris
        if self.tuileSelectionnee is not None:
            self.tuiles[self.tuileSelectionnee] = (event.x() // self.taille_case, event.y() // self.taille_case)
            self.update()

    def mouseReleaseEvent(self, event):
        # Gère le relâchement de la souris
        if self.tuileSelectionnee is not None:
            nouvelle_position = (event.x() // self.taille_case, event.y() // self.taille_case)
            positions_occupees = [pos for num, pos in self.tuiles.items() if num != self.tuileSelectionnee]
            if nouvelle_position not in positions_occupees:
                self.tuiles[self.tuileSelectionnee] = nouvelle_position
            else:
                # Si la nouvelle position est déjà occupée, remet la tuile à sa position originale
                self.tuiles[self.tuileSelectionnee] = self.positionOriginale
            self.tuileSelectionnee = None
            self.update()

    def paintEvent(self, event):
        # Dessine le damier et les tuiles
        painter = QPainter(self)
        painter.setFont(QFont('Arial', 12))  # Définit la police pour le texte des tuiles
        # Dessine le damier
        for ligne in range(15):
            for colonne in range(15):
                rect = QRect(colonne * self.taille_case, ligne * self.taille_case, self.taille_case, self.taille_case)
                painter.setBrush(self.couleur1 if (ligne + colonne) % 2 == 0 else self.couleur2)
                painter.drawRect(rect)
        # Dessine les tuiles sur le damier
        for numero, position in self.tuiles.items():
            x, y = position
            if numero == self.tuileSelectionnee:
                # Agrandit la tuile sélectionnée
                taille_tuile_agrandie = int(self.taille_case * self.agrandissement)
                decalage = (self.taille_case - taille_tuile_agrandie) // 2
                rect = QRect(x * self.taille_case + decalage, y * self.taille_case + decalage, taille_tuile_agrandie, taille_tuile_agrandie)
            else:
                rect = QRect(x * self.taille_case, y * self.taille_case, self.taille_case, self.taille_case)
            painter.setBrush(self.couleurTuile)
            painter.drawRect(rect)
            painter.drawText(rect, Qt.AlignCenter, str(numero))  # Numérote chaque tuile

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = Damier()
    fenetre.show()
    sys.exit(app.exec_())
