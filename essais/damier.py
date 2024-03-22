import sys
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QLabel
from PyQt5.QtGui import QPainter, QColor,QFont

class Damier(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Damier 15x15 avec tuiles rouges numérotées - PyQt5')
        self.setGeometry(100, 100, 600, 600)
        self.couleur1 = QColor(0, 0, 0)
        self.couleur2 = QColor(255, 255, 255)
        self.couleurTuile = QColor(255, 0, 0)
        self.taille_case = 40
        self.agrandissement = 1.1  # Facteur d'agrandissement de la tuile à 10%
        self.tuiles = {i: (i-1, 0) for i in range(1, 8)}  # Position initiale des tuiles numérotées de 1 à 7
        self.tuileSelectionnee = None
        self.taille_tuile = self.taille_case
        self.positionOriginale = None

    def mousePressEvent(self, event):
        x, y = event.x() // self.taille_case, event.y() // self.taille_case
        for numero, position in self.tuiles.items():
            if (x, y) == position:
                self.tuileSelectionnee = numero
                self.positionOriginale = position  # Stockez la position originale
                self.taille_tuile = int(self.taille_case * self.agrandissement)
                self.update()
                break

    def mouseMoveEvent(self, event):
        if self.tuileSelectionnee is not None:
            self.tuiles[self.tuileSelectionnee] = (event.x() // self.taille_case, event.y() // self.taille_case)
            self.update()

    def mouseReleaseEvent(self, event):
        if self.tuileSelectionnee is not None:
            nouvelle_position = (event.x() // self.taille_case, event.y() // self.taille_case)
            positions_occupées = [pos for num, pos in self.tuiles.items() if num != self.tuileSelectionnee]
            if nouvelle_position not in positions_occupées:
                self.tuiles[self.tuileSelectionnee] = nouvelle_position
            else:
            # Remet la tuile à sa position originale si la nouvelle position est occupée
                 self.tuiles[self.tuileSelectionnee] = self.positionOriginale
            self.tuileSelectionnee = None
            self.update()


    def paintEvent(self, event):
        painter = QPainter(self)
                # Dans votre méthode paintEvent, avant de dessiner les numéros sur les tuiles
        painter.setFont(QFont('Arial', 12))  # 'Arial' est le nom de la police, et 12 est la taille de la police
        for ligne in range(15):
            for colonne in range(15):
                rect = QRect(colonne * self.taille_case, ligne * self.taille_case, self.taille_case, self.taille_case)
                painter.setBrush(self.couleur1 if (ligne + colonne) % 2 == 0 else self.couleur2)
                painter.drawRect(rect)

        for numero, position in self.tuiles.items():
            x, y = position
            if numero == self.tuileSelectionnee:
                # Agrandit seulement la tuile sélectionnée
                taille_tuile_agrandie = int(self.taille_case * self.agrandissement)
                decalage = (self.taille_case - taille_tuile_agrandie) // 2
                rect = QRect(x * self.taille_case + decalage, y * self.taille_case + decalage, taille_tuile_agrandie, taille_tuile_agrandie)
            else:
                # Les tuiles non sélectionnées restent à leur taille originale
                rect = QRect(x * self.taille_case, y * self.taille_case, self.taille_case, self.taille_case)
            
            painter.setBrush(self.couleurTuile)
            painter.drawRect(rect)
            # Dessiner les numéros sur les tuiles, en ajustant le rectangle si nécessaire
            painter.drawText(rect, Qt.AlignCenter, str(numero))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = Damier()
    fenetre.show()
    sys.exit(app.exec_())
