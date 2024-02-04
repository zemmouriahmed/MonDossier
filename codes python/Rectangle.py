class Rectangle:
    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur
        

    def aire(self):
        return self.longueur * self.largeur
    
    def perimetre(self):
        return 2 * (self.longueur + self.largeur)
    
# création d'une instance de la classe Rectangle
my_rectangle = Rectangle (longueur=4,largeur=3)

#calcul et affichage de l'aire du rectangle
print("Aire du rectangle:", my_rectangle.aire())

#calcul et affichage du périmètre du rectangle
print("Périmètre du rectangle", my_rectangle.perimetre())