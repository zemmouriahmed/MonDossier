import tkinter as tk

# Configuration initiale
BOARD_SIZE = 15
TILE_SIZE = 40

def draw_grid(canvas, offset_x, offset_y):
    for i in range(BOARD_SIZE + 1):
        # Dessiner les lignes verticales avec le décalage
        canvas.create_line(offset_x + i*TILE_SIZE, offset_y, offset_x + i*TILE_SIZE, offset_y + BOARD_SIZE*TILE_SIZE)
        # Dessiner les lignes horizontales avec le décalage
        canvas.create_line(offset_x, offset_y + i*TILE_SIZE, offset_x + BOARD_SIZE*TILE_SIZE, offset_y + i*TILE_SIZE)

def main():
    root = tk.Tk()
    root.title("Tableau Quadrillé 15x15 Centré")

    # Définir la taille de la fenêtre en fonction de la taille du tableau et du nombre de cases
    window_size = BOARD_SIZE * TILE_SIZE * 2
    root.geometry(f"{window_size}x{window_size}")

    # Création du canvas
    canvas = tk.Canvas(root, width=window_size, height=window_size)
    canvas.pack()

    # Calculer le décalage pour centrer le tableau
    offset_x = (window_size - BOARD_SIZE * TILE_SIZE) // 2
    offset_y = (window_size - BOARD_SIZE * TILE_SIZE) // 2

    # Dessiner le quadrillage sur le canvas avec le décalage pour le centrer
    draw_grid(canvas, offset_x, offset_y)

    root.mainloop()

if __name__ == '__main__':
    main()
