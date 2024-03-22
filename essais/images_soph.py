from PIL import Image, ImageDraw, ImageFont
import os

# Créer le dossier 'bombage' s'il n'existe pas
dossier_images = 'bombage'
if not os.path.exists(dossier_images):
    os.makedirs(dossier_images)

def generer_image_lettre(lettre, dossier='bombage'):
    largeur, hauteur = 40, 40
    image = Image.new('RGB', (largeur, hauteur), '#003366')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("PermanentMarker-Regular.ttf", 40)
    
    # Dessiner l'ombre
    ombre_position = (largeur / 2 - 10, hauteur / 2 - 10)
    draw.text(ombre_position, lettre, fill="#000000", font=font)
    
    # Dessiner la lettre
    lettre_position = (largeur / 2 - 12, hauteur / 2 - 12)
    draw.text(lettre_position, lettre, fill="#FFFF00", font=font)
    
    chemin_sauvegarde = f"{dossier}/{lettre}.png"
    image.save(chemin_sauvegarde)
# Générer une image pour chaque lettre de l'alphabet
for lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    generer_image_lettre(lettre, dossier_images)

print("Les images des lettres ont été générées et sauvegardées dans le dossier 'bombage'.")
