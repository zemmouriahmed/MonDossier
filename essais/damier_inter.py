import tkinter as tk

class Damier(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Damier 15x15 avec tuiles rouges numérotées - Tkinter')
        self.geometry('600x640')
        self.couleur1 = 'black'
        self.couleur2 = 'white'
        self.couleurTuile = 'red'
        self.taille_case = 40
        self.agrandissement = 1.3  # Facteur d'agrandissement de la tuile à 30%
        self.tuiles = {i: (i-1, 15) for i in range(1, 8)}  # Position initiale des tuiles numérotées de 1 à 7
        self.tuileSelectionnee = None
        self.positionOriginale = None
        self.canvas = tk.Canvas(self, width=600, height=640)
        self.canvas.pack()
                
        self.bouton = tk.Button(self, text="Valider", command=self.action_bouton)
        position_x_bouton = 7 * self.taille_case
        position_y_bouton = 15 * self.taille_case  # La même ligne que les cases supplémentaires
        self.bouton.place(x=position_x_bouton, y=position_y_bouton, width=self.taille_case, height=self.taille_case)
        
        self.canvas.bind('<Button-1>', self.mousePressEvent)
        self.canvas.bind('<B1-Motion>', self.mouseMoveEvent)
        self.canvas.bind('<ButtonRelease-1>', self.mouseReleaseEvent)
        self.dessiner_damier()

        self.tuilesDeplacees = set()

        self.boutonFreeze = tk.Button(self.canvas, text="Freeze Tuiles", command=self.freezeTuiles)
        self.boutonFreeze.place(x=self.taille_case * 8, y=self.taille_case * 15, width=self.taille_case * 3, height=self.taille_case)

    def freezeTuiles(self):
        # Exemple d'action : "Fige" les tuiles en les rendant non déplaçables
        self.tuilesDeplacees.clear()  # Rend toutes les tuiles à nouveau déplaçables; utiliser set() pour figer
        self.dessiner_damier()


    def action_bouton(self):
        # Définissez ce que doit faire le bouton ici
        print("Le bouton a été cliqué")


    def mousePressEvent(self, event):
        x, y = event.x // self.taille_case, event.y // self.taille_case
        for numero, position in self.tuiles.items():
            if (x, y) == position:
                self.tuileSelectionnee = numero
                self.positionOriginale = position
                self.dessiner_damier()
                break

    def mouseMoveEvent(self, event):
        if self.tuileSelectionnee is not None:
            self.tuiles[self.tuileSelectionnee] = (event.x // self.taille_case, event.y // self.taille_case)
            self.dessiner_damier()

    def mouseReleaseEvent(self, event):
        if self.tuileSelectionnee is not None:
            self.tuiles[self.tuileSelectionnee] = (event.x // self.taille_case, event.y // self.taille_case)
            self.tuileSelectionnee = None
            self.dessiner_damier()


    def dessiner_damier(self):
        self.canvas.delete("all")
        for ligne in range(15):
            for colonne in range(15):
                x0 = colonne * self.taille_case
                y0 = ligne * self.taille_case
                x1 = x0 + self.taille_case
                y1 = y0 + self.taille_case
                couleur = self.couleur1 if (ligne + colonne) % 2 == 0 else self.couleur2
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=couleur, outline='')

    # Dessinez la ligne supplémentaire de 7 cases
        ligne_suppl = 15  # La ligne supplémentaire est juste après la dernière ligne du damier
        for colonne in range(7):  # Seulement 7 cases dans cette ligne
            x0 = colonne * self.taille_case
            y0 = ligne_suppl * self.taille_case
            x1 = x0 + self.taille_case
            y1 = y0 + self.taille_case
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.couleur2, outline='black')  # Utilisez couleur2 pour ces cases


        for numero, position in self.tuiles.items():
            x, y = position
            x0 = x * self.taille_case
            y0 = y * self.taille_case
            x1 = x0 + self.taille_case
            y1 = y0 + self.taille_case
            if numero == self.tuileSelectionnee:
                taille = self.taille_case * self.agrandissement
                decalage = (self.taille_case - taille) // 2
                self.canvas.create_rectangle(x0 - decalage, y0 - decalage, x1 + decalage, y1 + decalage, fill=self.couleurTuile, outline='')
            else:
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.couleurTuile, outline='')
            self.canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text=str(numero), fill='black')

if __name__ == '__main__':
    app = Damier()
    app.mainloop()
