import sys
from PyQt5.QtCore import QRect, Qt, QPoint, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QLabel, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPainter, QColor,QFont
from lettres import SacDeLettres


class Tuile(QLabel):
    def __init__(self, numero, parent=None):
        super().__init__(parent)
        self.numero = numero
        self.setText(str(numero))
        self.setFixedSize(40, 40)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("background-color: red; color: white; border-radius: 5px;")
        self.original_size = QSize(40, 40)
        self.drag_start_position = None
        self.setMouseTracking(True)  # Active le suivi de la souris
        self.original_position = None

        font = QFont('Arial',12)
        self.setFont(font)
        self.updateStyle()
        self.setEffect()

        self.position_initiale = None # Sauvegarde de la position initiale
        self.figee = False  # Par défaut, les tuiles ne sont pas figées

    def isDeplacable(self):
        return not self.figee  # Une tuile est déplaçable si elle n'est pas figée

    def figerSiDeplacee(self):
        if self.pos() != self.position_initiale:
            self.figee = True  # Figer la tuile si sa position a changé

    def setEffect(self, moving=False):
        ombre = QGraphicsDropShadowEffect(self)
        ombre.setColor(QColor(0, 0, 0, 150))
        if moving:
            # Création et application de l'effet d'ombre lors du déplacement
            ombre = QGraphicsDropShadowEffect()
            ombre.setBlurRadius(25)  # Ajustez ces valeurs selon l'effet désiré
            ombre.setXOffset(15)
            ombre.setYOffset(15)
            ombre.setColor(QColor(0, 0, 0, 100))
            self.setGraphicsEffect(ombre)
            # Augmenter la taille de la tuile de 15%
            new_width = int(self.original_size.width() * 1.15)
            new_height = int(self.original_size.height() * 1.15)
            self.setFixedSize(new_width, new_height)
        else:

            # Réinitialiser la taille à la taille originale
            self.setFixedSize(self.original_size)
            self.setGraphicsEffect(None)
    
        self.updateStyle(moving)


    def updateStyle(self, moving=False):
        if moving:
            self.setStyleSheet("background-color: #ff5555; color: white; border-radius: 5px;")  # Plus lumineux
        else:
            self.setStyleSheet("background-color: red; color: white; border-radius: 5px;")


    def mousePressEvent(self, event):
        if self.isDeplacable():
            if event.button() == Qt.LeftButton:
                self.drag_start_position = event.pos()
                self.original_position = self.pos()  # Sauvegarde de la position actuelle
                self.raise_()  # Met la tuile au premier plan
                self.setEffect(True)  # Activer les effets de déplacement

            pass


    def mouseMoveEvent(self, event):
        if self.isDeplacable():
            if event.buttons() == Qt.LeftButton and self.drag_start_position is not None:
                drag_distance = event.pos() - self.drag_start_position
                self.move(self.pos() + drag_distance)

            pass


   
    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)  # Assurez-vous d'appeler la méthode parent si nécessaire
        if self.drag_start_position is not None:
            parent = self.parent()
            if isinstance(parent, Damier):
                snapped_position = parent.calculateSnappedPosition(self.pos(), self.original_position)
                self.move(snapped_position)
            self.setEffect(False)  # Désactiver les effets de déplacement
            self.drag_start_position = None



class Damier(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SCRABBLE WITH ZEM')
                # Créez et configurez le widget damier ici
       
        # Ajustez la taille de la fenêtre principale pour inclure l'espace supplémentaire
        self.setGeometry(100, 100, 800, 850)  # Ajoute 100 pixels d'espace supplémentaire en bas
        self.taille_case = 40  # Ajoutez cette ligne pour définir la taille des cases

        self.nombre_cases = 15  # 15x15 cases


        self.sac_de_lettres = SacDeLettres()  # Initialisation du sac de lettres
        self.tuiles = []  # Liste pour

        # Initialiser la zone de tirage
        self.initZoneTirage()
      
        self.configurerBoutons()
        self.tirage_initial()  # Effectuez le tirage initial de 7 lettres






          # Définition des cases spéciales
        self.cases_speciales = {
            'MD': [(1, 1), (1, 13), (2, 2), (2, 12), (3, 3), (3, 11), (4, 4),
                      (4, 10), (7, 7), (10, 4), (10, 10), (11, 3), (11, 11),
                      (12, 2), (12, 12), (13, 1), (13, 13)],  # Exemple de positions Mot Double
            'MT': [(0, 0), (0, 7), (0, 14), (7, 0), (7, 14), (14, 0), (14, 7),
                      (14, 14)],  # Mot Triple
            'LD': [(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14),
                         (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8, 2),
                         (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6),
                         (12, 8), (14, 3), (14, 11)],  # Lettre Double
            'LT': [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1),
                         (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)],  # Lettre Triple
        }

        self.colors = {
            'MD': QColor(255, 153, 51),  # Orange
            'MT': QColor(255, 51, 51),   # Rouge
            'LD': QColor(102, 204, 255), # Bleu clair
            'LT': QColor(51, 51, 255),   # Bleu foncé
            'normal': QColor(255, 255, 255)  # Blanc
        }

        # Configuration des boutons
        self.configurerBoutons()





    def configurerBoutons(self):
        # Bouton "Valider position"
        self.boutonValider = QPushButton("Valider", self)
        self.boutonValider.setGeometry(200, 650, 100, 20)  # Ajustez la position et la taille
        self.boutonValider.setStyleSheet("background-color: red; color: white;")
        font = QFont("Arial", 12)  # Choisir la famille de la police et la taille
        self.boutonValider.setFont(font)




        # Bouton "Nouveau tirage"
        self.boutonNouveau = QPushButton("tirer", self)
        self.boutonNouveau.setGeometry(500, 650, 100, 20)  # Ajustez la position et la taille
        self.boutonNouveau.setStyleSheet("background-color: green; color: white;")
        font = QFont("Arial", 12)  # Choisir la famille de la police et la taille
        self.boutonNouveau.setFont(font)





        # Connecter les signaux à des slots pour gérer les clics sur les boutons
        self.boutonValider.clicked.connect(self.onValiderClicked)
        self.boutonNouveau.clicked.connect(self.onNouveauClicked)
        

    def initZoneTirage(self):
    
        largeur_zone_tirage = 280  # Ou calculez en fonction du nombre de tuiles et de leur taille
        hauteur_zone_tirage = 40
        x_zone_tirage = (self.width() - largeur_zone_tirage) // 2
        y_zone_tirage = self.height() - hauteur_zone_tirage - 100  # Ajustez -100 pour la position par rapport au bas
        self.widgetZoneTirage = QWidget(self)
        self.layoutZoneTirage = QHBoxLayout(self.widgetZoneTirage)  # Utilisez QHBoxLayout pour organiser les tuiles horizontalement

        self.widgetZoneTirage.setGeometry(x_zone_tirage, y_zone_tirage, largeur_zone_tirage, hauteur_zone_tirage)
        self.widgetZoneTirage.setStyleSheet("border: 1px solid black; background-color: white;")

        largeur_totale = self.widgetZoneTirage.width()  # Assurez-vous que ceci est défini correctement
        largeur_case = int(largeur_totale / 7)  # Conversion explicite en int
        
        for i in range(7):  # Pour créer 7 partitions
            partition = QLabel(self.widgetZoneTirage)
            partition.setGeometry(i * largeur_case, 0, largeur_case, self.widgetZoneTirage.height())
            partition.setStyleSheet("border-right: 1px solid black;")
            
        # Assurez-vous de ne pas dessiner une bordure à droite pour la dernière partition
        if i == 6:
            partition.setStyleSheet("")

    def tirage_initial(self):
            lettres_tirees = self.sac_de_lettres.tirer_lettres(7)  # Tire 7 lettres du sac
            for lettre_info in lettres_tirees:
                tuile = Tuile(lettre_info['letter'], self.widgetZoneTirage)  # Créez une tuile pour chaque lettre
                self.layoutZoneTirage.addWidget(tuile)  # Ajoutez la tuile à la zone de tirage
                self.tuiles.append(tuile)  # Ajoutez la tuile à la liste des tuiles pour une gestion future


            
    def onValiderClicked(self):
        for tuile in self.tuiles:  # Supposons que `self.tuiles` est une liste de toutes vos instances de `Tuile`
            tuile.figerSiDeplacee()

        
    def onNouveauClicked(self):
        # Logique à exécuter lorsque "Nouveau tirage" est cliqué
        print("Nouveau tirage")


    def calculateSnappedPosition(self, position, original_position):
        # Calcul de la position ajustée
        x = round(position.x() / self.taille_case) * self.taille_case
        y = round(position.y() / self.taille_case) * self.taille_case
        snapped_position = QPoint(x, y)
        
        # Vérification des limites du damier
        if x < 0 or x >= self.widgetDamier.width() or y < 0 or y >= self.widgetDamier.height():
            return original_position  # Retour à la position originale si hors limites
        
        # Vérification de la superposition
        for tuile in self.tuiles:
            if tuile.pos() == snapped_position and tuile.pos() != original_position:
                return original_position  # Retour à la position originale si superposition détectée
        
        return snapped_position

            
   

    def initTuiles(self):
        for i in range(1, 8):
            tuile = Tuile(i, self)
            tuile.move((i-1) * self.taille_case, 0)  # Position initiale des tuiles
            tuile.position_initiale = tuile.pos()
            tuile.show()
            self.tuiles.append(tuile)




    def paintEvent(self, event):
        painter = QPainter(self)
        largeur_damier = self.taille_case * self.nombre_cases  # Largeur totale du damier
        x_damier = (self.width() - largeur_damier) // 2  # Calcul du nouveau point de départ x pour centrer le damier
        
        for ligne in range(15):
            for colonne in range(15):
                # Ajustement de la position x de chaque case en fonction du nouveau point de départ x
                rect = QRect(x_damier + colonne * self.taille_case, ligne * self.taille_case, self.taille_case, self.taille_case)
                
                # Déterminer la couleur de la case
                color = self.colors['normal']  # Couleur par défaut
                label = ""  # Texte à afficher sur la case
                text_color = QColor(0,0,0)

                for type_case, positions in self.cases_speciales.items():
                    if (ligne, colonne) in positions:
                        color = self.colors[type_case]
                        if type_case == 'MD':
                            label = "DW"
                        elif type_case == 'MT':
                            label = "TW"

                        elif type_case == 'LD':
                            label = "DL"
                        elif type_case == 'LT':
                            label = "TL"

                        break
                
                painter.setBrush(color)
                painter.drawRect(rect)

                # Affichage du texte sur la case
                if label:
                    painter.setPen(text_color)  # Couleur du texte
                    font = QFont('Arial', 12, QFont.Bold)  # Définit la police avec Arial, taille 8, et en gras

                    painter.setFont(font)
                    painter.drawText(rect, Qt.AlignCenter, label)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = Damier()
    fenetre.show()
    sys.exit(app.exec_())
