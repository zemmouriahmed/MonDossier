 

import random



sac_tuiles = [
    {'lettre': 'A', 'value': 1, 'quantity': 9},
    {'lettre': 'B', 'value': 3, 'quantity': 2},
    {'lettre': 'C', 'value': 3, 'quantity': 2},
    {'lettre': 'D', 'value': 2, 'quantity': 4},
    {'lettre': 'E', 'value': 1, 'quantity': 12},
    {'lettre': 'F', 'value': 4, 'quantity': 2},
    {'lettre': 'G', 'value': 2, 'quantity': 3},
    {'lettre': 'H', 'value': 4, 'quantity': 2},
    {'lettre': 'I', 'value': 1, 'quantity': 9},
    {'lettre': 'J', 'value': 8, 'quantity': 1},
    {'lettre': 'K', 'value': 10, 'quantity': 1},
    {'lettre': 'L', 'value': 1, 'quantity': 4},
    {'lettre': 'M', 'value': 2, 'quantity': 2},
    {'lettre': 'N', 'value': 1, 'quantity': 6},
    {'lettre': 'O', 'value': 1, 'quantity': 8},
    {'lettre': 'P', 'value': 3, 'quantity': 2},
    {'lettre': 'Q', 'value': 10, 'quantity': 1},
    {'lettre': 'R', 'value': 1, 'quantity': 6},
    {'lettre': 'S', 'value': 1, 'quantity': 4},
    {'lettre': 'T', 'value': 1, 'quantity': 6},
    {'lettre': 'U', 'value': 1, 'quantity': 4},
    {'lettre': 'V', 'value': 4, 'quantity': 2},
    {'lettre': 'W', 'value': 4, 'quantity': 2},
    {'lettre': 'X', 'value': 8, 'quantity': 1},
    {'lettre': 'Y', 'value': 4, 'quantity': 2},
    {'lettre': 'Z', 'value': 10, 'quantity': 1},
    {'lettre': '*', 'value': 0, 'quantity': 2},  # Joker
]



class Tuile:
    def __init__(self, lettre, valeur):
        self.lettre = lettre
        self.valeur = valeur
        self.x = None
        self.y = None
        self.prev_x = None
        self.prev_y = None
        self.gelee = False

    def placer_sur_plateau(self, x, y):
        # Verify if the position is within the board and not occupied.
        if not plateau.est_case_occupee(x, y) and not self.gelee:
            self.prev_x = self.x
            self.prev_y = self.y
            self.x = x
            self.y = y
        else:
            self.x = self.prev_x if self.prev_x is not None else self.x
            self.y = self.prev_y if self.prev_y is not None else self.y
    def geler(self):
        self.gelee = True

    def __repr__(self):
        return f"Tuile({self.lettre}, {self.valeur}, Position: {self.x},{self.y}, Gelée: {self.gelee})"


class SacDeTuiles:
    def __init__(self, sac_tuiles):
        self.tuiles = self._initialiser_tuiles(sac_tuiles)

    def _initialiser_tuiles(self, sac_tuiles):
        tuiles = []
        for item in sac_tuiles:
            for _ in range(item['quantity']):
                tuiles.append(Tuile(item['lettre'], item['value']))
        random.shuffle(tuiles)
        return tuiles

    def tirer_tuiles(self, nombre):
        tirage = self.tuiles[:nombre]
        self.tuiles = self.tuiles[nombre:]
        return tirage


