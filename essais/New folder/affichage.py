# affichage.py
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QColor, QFont, QPainter, QMouseEvent
from PyQt5.QtCore import QRect, Qt
from mouvement import GestionDeplacement
from bouton import BottomButton

class AffichagePlateau(QMainWindow):
    def __init__(self, cases_speciales, plateau, taille_case=40):
        super().__init__()
        self.setWindowTitle('Grid with Coordinate Identifiers - PyQt5')
        self.setGeometry(100, 100, 600, 640)  # Window size for 16 rows and 15 columns
        self.taille_case = taille_case

        # Stockage des données nécessaires pour l'affichage
        self.cases_speciales = cases_speciales
        self.plateau = plateau

        self.gestion_deplacement = GestionDeplacement(plateau, self.update)
       
       
       # Initialisation et positionnement du bouton
        self.initBottomButton()

    def initBottomButton(self):
        # Création du bouton et définition de sa taille pour couvrir les 8 dernières cases
        self.bottomButton = BottomButton(self)
        self.bottomButton.setGeometry(7 * self.taille_case, 15 * self.taille_case, 8 * self.taille_case, self.taille_case)
        self.bottomButton.show()

    def mousePressEvent(self, event: QMouseEvent):
        # Transmet l'événement à la classe de gestion de déplacement
        self.gestion_deplacement.handle_mouse_press(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        # Transmet l'événement à la classe de gestion de déplacement
        self.gestion_deplacement.handle_mouse_move(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        # Transmet l'événement à la classe de gestion de déplacement
        self.gestion_deplacement.handle_mouse_release(event)




    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), QColor(255, 255, 255))  # White background
        font = QFont('Arial', 10)
        painter.setFont(font)

        # Draw the grid and special cells first
        for y in range(16):
            for x in range(15):
                rect = QRect(x * self.taille_case, y * self.taille_case, self.taille_case, self.taille_case)
                if (x, y) in self.cases_speciales:
                    couleur, inscription = self.cases_speciales[(x, y)]
                    painter.setBrush(QColor(couleur))
                else:
                    painter.setBrush(QColor(240, 240, 240))  # Default grid color
                painter.drawRect(rect)

                # Draw the inscription for special cells
                if (x, y) in self.cases_speciales:
                    painter.setPen(QColor(0, 0, 0))  # Text color
                    painter.drawText(rect, Qt.AlignCenter, inscription)

        # Draw all stationary tiles
        for y in range(16):
            for x in range(15):
                rect = QRect(x * self.taille_case, y * self.taille_case, self.taille_case, self.taille_case)
                tuile = self.plateau.plateau[y][x]
                if tuile and not (hasattr(tuile, 'temp_x') or hasattr(tuile, 'temp_y')):
                    painter.setBrush(QColor('#00008B'))  # Tile color
                    painter.setPen(QColor('#FFFF00'))  # Text color
                    painter.drawRect(rect)
                    painter.drawText(rect, Qt.AlignCenter, tuile.lettre)

        # Draw the moving tile last
        moving_tile = None
        for y in range(16):
            for x in range(15):
                tuile = self.plateau.plateau[y][x]
                if tuile and (hasattr(tuile, 'temp_x') or hasattr(tuile, 'temp_y')):
                    moving_tile = tuile  # Identify the moving tile

        if moving_tile:
            rect = QRect(int(moving_tile.temp_x), int(moving_tile.temp_y), self.taille_case, self.taille_case)
            painter.setBrush(QColor('#00008B'))
            painter.setPen(QColor('#FFFF00'))
            painter.drawRect(rect)
            painter.drawText(rect, Qt.AlignCenter, moving_tile.lettre)

        super().paintEvent(event)
