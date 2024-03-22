import sys
from tableau import Plateau, run
from infos import InfoWindow
from PyQt5.QtWidgets import QApplication
import tableau  # Assurez-vous que tableau.py est dans le même dossier que main.py
from tuiles import SacDeTuiles, sac_tuiles
from tirage_tuiles import effectuer_tirage


class MainApplication:
    def __init__(self, app):
        self.app = app

        self.plateau = Plateau()
        
        tuiles_positionnees = effectuer_tirage()
        self.plateau.placer_tuiles(tuiles_positionnees)

        self.fenetre_principale = run(self.plateau.cases_speciales, self.plateau, self.plateau.taille_case)
        self.fenetre_infos = InfoWindow(self.fenetre_principale)
        self.fenetre_infos.show()

    def run(self):
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApplication(app)
    main_app.run()