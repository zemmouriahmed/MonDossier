
from PyQt5.QtGui import QMouseEvent



class GestionDeplacement:
    def __init__(self, plateau, update_callback):

        self.plateau = plateau
        self.update_callback = update_callback
        self.tuileSelectionnee = None
        self.positionOriginale = None

    def handle_mouse_press(self, event: QMouseEvent):
        print(type(self.plateau))  # Affiche le type de self.plateau pour vérifier qu'il s'agit bien de l'instance Plateau.

        x, y = event.x() // self.plateau.taille_case, event.y() // self.plateau.taille_case
        if self.plateau.est_case_occupee(x, y):
            tuile = self.plateau.plateau[y][x]
            if tuile and not tuile.gelee:
                self.tuileSelectionnee = tuile
                self.positionOriginale = (tuile.x, tuile.y)

    def handle_mouse_move(self, event: QMouseEvent):
        if self.tuileSelectionnee:
            # Directly use mouse coordinates without aligning to grid cells.
            # This allows for free movement, giving the feeling of dragging the tile.
            self.tuileSelectionnee.temp_x = event.x() - (self.plateau.taille_case / 2)
            self.tuileSelectionnee.temp_y = event.y() - (self.plateau.taille_case / 2)
            self.update_callback()  # Invoke the update to redraw the display.

    def handle_mouse_release(self, event: QMouseEvent):
        if self.tuileSelectionnee:
            # Calculate the grid position for the released tile.
            new_x = round((event.x() - (self.plateau.taille_case / 2)) / self.plateau.taille_case)
            new_y = round((event.y() - (self.plateau.taille_case / 2)) / self.plateau.taille_case)

            # Ensure the snapped position is within the bounds of the grid.
            new_x = max(0, min(new_x, 14))
            new_y = max(0, min(new_y, 15))

            # Enforce the constraint that a tile cannot be placed in the last 8 cells of the bottom row.
            if new_y == 15 and new_x >= 7:
                self.plateau.déplacer_tuile(self.tuileSelectionnee, self.positionOriginale, self.positionOriginale)
            elif not self.plateau.est_case_occupee(new_x, new_y) or (self.positionOriginale == (new_x, new_y)):
                # Move the tile if the new position is valid and not restricted.
                self.plateau.déplacer_tuile(self.tuileSelectionnee, self.positionOriginale, (new_x, new_y))
            else:
                # If the target position is occupied or invalid, revert to the original position.
                self.plateau.déplacer_tuile(self.tuileSelectionnee, self.positionOriginale, self.positionOriginale)

            # Clear the temporary attributes after releasing the tile.
            if hasattr(self.tuileSelectionnee, 'temp_x'):
                delattr(self.tuileSelectionnee, 'temp_x')
            if hasattr(self.tuileSelectionnee, 'temp_y'):
                delattr(self.tuileSelectionnee, 'temp_y')

            self.tuileSelectionnee = None
            self.update_callback()
