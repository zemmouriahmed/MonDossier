from tuiles import SacDeTuiles, sac_tuiles

class GestionTuiles:
    def __init__(self):
        # Initialisation du sac de tuiles
        self.sac = SacDeTuiles(sac_tuiles)
        
    def tirer_tuiles(self, nombre=7):
        # Tirage des tuiles
        return self.sac.tirer_tuiles(nombre)

    def placer_tuiles_initiales(self, tuiles):
        # Ici, vous pourriez définir la logique de placement ou juste préparer les tuiles
        # La fonction pourrait être enrichie pour interagir avec le plateau.
        # Exemple : mise à jour des positions (x, y) des tuiles pour la zone de tirage
        for i, tuile in enumerate(tuiles):
            # Définit les positions x, y pour la zone de tirage (ligne 15, colonnes 0 à 6)
            tuile.x, tuile.y = i, 15
        # Ici, vous pourriez avoir besoin de retourner les tuiles avec leurs nouvelles positions,
        # ou de les envoyer directement à une fonction de mise à jour du plateau.
        return tuiles

# Dans tirage_tuiles.py

def effectuer_tirage():
    gestion_tuiles = GestionTuiles()
    tuiles_tirees = gestion_tuiles.tirer_tuiles()
    tuiles_positionnees = gestion_tuiles.placer_tuiles_initiales(tuiles_tirees)
    return tuiles_positionnees

if __name__ == "__main__":
    tuiles_positionnees = effectuer_tirage()
    for tuile in tuiles_positionnees:
        print(f"{tuile.lettre} placée en position ({tuile.x}, {tuile.y})")
