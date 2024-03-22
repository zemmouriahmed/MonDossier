from PIL import Image, ImageTk
import tkinter as tk
from lettres import SacDeLettres


# Configuration initiale
BOARD_SIZE = 15
TILE_SIZE = 40
SPECIAL_TILES = {
            'MD': [(1, 1), (1, 13), (2, 2), (2, 12), (3, 3), (3, 11), (4, 4),
                      (4, 10), (7, 7), (10, 4), (10, 10), (11, 3), (11, 11),
                      (12, 2), (12, 12), (13, 1), (13, 13)],  # Exemple de positions Mot Double
            'MT': [(0, 0), (0, 7), (0, 14), (7, 0), (7, 14), (14, 0), (14, 7),
                      (14, 14)],  # Mot Triple
            'LD': [(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14),
                         (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8, 2),
                         (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6),
                         (12, 8), (14, 3), (14, 11)],  # Lettre Double
            'LT': [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1),
                         (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)],  # Lettre Triple
}


# Fonction pour déterminer la couleur et le texte d'une case
def get_special_tile_details(x, y):
    for special_type, positions in SPECIAL_TILES.items():
        if (x, y) in positions:
            if special_type == 'MD':
                return 'lightblue', 'MD'
            elif special_type == 'MT':
                return 'pink', 'MT'
            elif special_type == 'LD':
                return 'lightgreen', 'LD'
            elif special_type == 'LT':
                return 'orange', 'LT'
    return 'white', ''


def create_tile(canvas, x, y, is_drawing_tile=False, letter=None):
    # Cette fonction a été légèrement modifiée pour accepter un paramètre 'letter'
    if is_drawing_tile:
        background_color = '#D400FF'
        text_color =  'black'
        text = letter['letter'] if letter else '' # Utilise la lettre tirée
        font = ("Caveat", 14, "bold")
        
    else:
        # Pour le plateau de jeu, déterminez la case spéciale
        background_color, text = get_special_tile_details(x, y)
        text_color = "black"
        font = ("Helvetica", 12)
    canvas.create_rectangle(x * TILE_SIZE, y * TILE_SIZE, (x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE, fill=background_color, outline='black')
    if text:
        canvas.create_text(x * TILE_SIZE + TILE_SIZE/2, y * TILE_SIZE + TILE_SIZE/2, text=text,  fill=text_color, font=font)


def main():

    # Calcul du décalage horizontal pour centrer le plateau dans la fenêtre
    offset_x_plateau = (800 - (BOARD_SIZE * TILE_SIZE)) // 2
    
    # Calcul de la position y de la zone de tirage pour la positionner en dessous du plateau
    offset_y_draw_zone = BOARD_SIZE * TILE_SIZE + 10  # +10 pour un peu d'espace entre le plateau et la zone de tirage


    root = tk.Tk()
    root.title("SCRABBLE WITH ZEM")
    root.geometry("800x800")

     # Création du sac de lettres
    sac = SacDeLettres()
    
    # Création du plateau de jeu, centré dans la fenêtre
    board_canvas = tk.Canvas(root, width=BOARD_SIZE*TILE_SIZE, height=BOARD_SIZE*TILE_SIZE)
    board_canvas.pack(side=tk.TOP, padx=offset_x_plateau, pady=(5,0))  # Utilisez offset_x_plateau pour centrer le plateau




    # Initialisation du plateau de jeu avec cases spéciales
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            create_tile(board_canvas, x, y)


    # Création de la zone de tirage, centrée par rapport au plateau et positionnée correctement en dessous
    draw_canvas = tk.Canvas(root, width=7*TILE_SIZE, height=TILE_SIZE)
    draw_canvas.place(x=offset_x_plateau + ((BOARD_SIZE*TILE_SIZE - 7*TILE_SIZE) // 2), y=offset_y_draw_zone)  # Centrage basé sur les calculs

   
   
   
    # Tirer 7 lettres du sac
    lettres_tirees = sac.tirer_lettres(7)
    
    # Afficher les lettres tirées dans la zone de tirage
    for i, lettre in enumerate(lettres_tirees):
        create_tile(draw_canvas, i, 0, letter=lettre, is_drawing_tile=True)


        
    root.mainloop()

if __name__ == '__main__':
    main()
