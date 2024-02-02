class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def recup_coordonnées(self):
        return(self.x,self.y,self.z)
    
# création d'une instance de la classe Point3D
my_point = Point3D(x=1,y=2,z=3)

#affichage des coordonnées de my_point
print(my_point.recup_coordonnées())