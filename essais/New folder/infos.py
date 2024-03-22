from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel, QListWidget

class InfoWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Informations de la Partie")  # Titre de la fenêtre
        self.setGeometry(800, 100, 400, 640)  # Position et dimensions : x, y, largeur, hauteur

        self.layout = QGridLayout(self)

        # Configuration des sections de la grille
        self.layout.addWidget(QLabel("Scores:"), 0, 0, 1, 2)
        self.layout.addWidget(QLabel("Joueur 1"), 1, 0)
        self.layout.addWidget(QLabel("Joueur 2"), 1, 1)

        # Configuration des labels pour les scores
        self.scoreLabel1 = QLabel("0")
        self.scoreLabel2 = QLabel("0")
        self.layout.addWidget(self.scoreLabel1, 2, 0)
        self.layout.addWidget(self.scoreLabel2, 2, 1)

        # Configuration des listes pour les mots joués
        self.layout.addWidget(QLabel("Mots Joués:"), 3, 0, 1, 2)
        self.wordsList1 = QListWidget()
        self.wordsList2 = QListWidget()
        self.layout.addWidget(self.wordsList1, 4, 0)
        self.layout.addWidget(self.wordsList2, 4, 1)

        # Configuration de l'affichage des tuiles restantes
        self.tilesLabel = QLabel("Tuiles restantes: 100")
        self.layout.addWidget(self.tilesLabel, 5, 0, 1, 2)

    def updateScores(self, player1_score, player2_score):
        self.scoreLabel1.setText(str(player1_score))
        self.scoreLabel2.setText(str(player2_score))

    def updateWords(self, player1_words, player2_words):
        self.wordsList1.clear()
        self.wordsList2.clear()
        for word in player1_words:
            self.wordsList1.addItem(word)
        for word in player2_words:
            self.wordsList2.addItem(word)

    def updateTileCount(self, tile_count):
        self.tilesLabel.setText(f"Tuiles restantes: {tile_count}")
