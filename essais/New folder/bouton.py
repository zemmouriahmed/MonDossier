from PyQt5.QtWidgets import QPushButton, QDialog, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import QSize, Qt

class PopupDialog(QDialog):
    def __init__(self, mot='', score=0, valide=True):
        super().__init__()
        self.setWindowTitle("Popup Dialog")
        self.setFixedSize(QSize(600, 600))  # Taille ajustée pour mieux accueillir les boutons carrés

        layout = QVBoxLayout(self)


        # Informations sur le mot, le score et la validité
        mot_label = QLabel(f"Mot formé : {mot}")
        mot_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(mot_label)

        score_label = QLabel(f"Score du mot : {score} points")
        score_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(score_label)

        statut = "Valide" if valide else "Invalide"
        statut_label = QLabel(f"Statut : {statut} selon le dictionnaire")
        statut_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(statut_label)


        buttons_layout = QHBoxLayout()



        # Bouton 'Valider'
        valider_button = QPushButton('Valider', self)
        valider_button.setStyleSheet("""
            QPushButton {
            background-color: #00008B;
            color: #FFFF00;
            font-family: 'Arial';
            font-size: 34pt;
                                     
            min-width: 70px; 
            min-height: 70px;  
            border-radius: 5px;  
            padding: 10px;  
            letter-spacing: 1px;  
                     }
        """)
        valider_button.clicked.connect(self.accept)
        buttons_layout.addWidget(valider_button)

        # Bouton 'Annuler et modifier'
        annuler_button = QPushButton('Annuler\n et\n modifier', self)
        annuler_button.setStyleSheet("""
            QPushButton {
            background-color: red;
            color: #FFFFFF;  
            font-family: 'Arial';
            font-size: 12pt;  
            min-width: 70px;  
            min-height: 70px;  
            border-radius: 5px;  
            padding: 10px;   
            letter-spacing: 1px;  
                                     }
        """)
        annuler_button.clicked.connect(self.reject)
        buttons_layout.addWidget(annuler_button)

        layout.addLayout(buttons_layout)


# Définition de la classe BottomButton qui ouvre la PopupDialog
class BottomButton(QPushButton):
    def __init__(self, parent=None, mot='', score=0, valide=True):
        super().__init__(parent)
        self.setText("VALIDER TOUR")
        self.setStyleSheet("""
            QPushButton {
                background-color: #00008B;
                color: #FFFF00;
                font-family: 'Arial';
                font-size: 10pt;
                letter-spacing: 2px;
            }
        """)
        self.mot = mot
        self.score = score
        self.valide = valide
        self.clicked.connect(self.showDialog)

    def showDialog(self):

        # Méthode pour afficher la boîte de dialogue.
        dialog = PopupDialog(self.mot, self.score, self.valide)
        dialog.exec_()
