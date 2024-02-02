#Pour calculer la surface d'un cercle, nous allons avoir besoin de la constante PI. Pour ce faire, nous allons importer le module math.
#Ce module contient beaucoup d'autres constantes et formules

import math
from typing import Any

class Cercle:
    def __init__(self, centre_x,centre_y,rayon):
        self.centre_x = centre_x
        self.centre_y = centre_y
        self.rayon = rayon
# nous venons de définir le centre du cercle par ses coordonnées
# et le rayon par lui-même
# cette définition facilitera la résolution de la seconde partie du problème
# qui est celle de savoir si un point est situé à l'intérieur
# du périmètre du cercle
        
    def aire(self):
        return math.pi * (self.rayon**2)
    
    def perimetre(self):
        return 2 * math.pi * self.rayon
    
    def isInside(self, point_x, point_y):
        hypotenuse_carre = (point_x - self.centre_x)**2 + (point_y - self.centre_y)**2
        return hypotenuse_carre <= self.rayon**2
    
    def __str__(self):
        return f"Cercle de centre({self.centre_x},{self.centre_y}) et de rayon {self.rayon}"

# Création d'une instance de la classe Cercle
centre_x = float(input("entrer la coordonnée x du centre du cercle :"))
centre_y = float(input("Entrer la coordonnée y du centre du cercle :"))
rayon = float(input("Entrer le rayon du cercle :"))
my_cercle = Cercle(centre_x, centre_y, rayon)

# Caractéristiques du cercle
print(my_cercle)

# Demander à l'utilisateur de saisir les coordonnées d'un point
point_x = float(input("Entrer la coordonnée x du point :"))
point_y = float(input("Entrer la coordonnée y du point :"))

#Vérification de la position du point
point_dans_cercle = my_cercle.isInside(point_x, point_y)

if point_dans_cercle :
    print(f"le point ({point_x}, {point_y}) est à l'intérieur du cercle.")
else:
    print(f"le point ({point_x}, {point_y}) n'est pas à l'intérieur du cercle.")
  