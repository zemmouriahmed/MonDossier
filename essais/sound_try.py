from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import sys

class AudioPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Créer l'instance de QMediaPlayer
        self.player = QMediaPlayer()
        
        # Charger le fichier son
        url = QUrl.fromLocalFile("chemin/vers/votre/fichier/son.mp3")
        content = QMediaContent(url)
        self.player.setMedia(content)
        
        # Jouer le son
        self.player.play()

def main():
    app = QApplication(sys.argv)
    player = AudioPlayer()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
