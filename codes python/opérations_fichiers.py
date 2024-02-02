def lire_fichier_entier(nom_fichier):
    """Lire le contenu entier d'un fichier."""
    try:
        with open(nom_fichier,'r',encoding='utf-8') as fichier:
            contenu = fichier.read()
            print(f"Contenu du fichier{nom_fichier}:\n{contenu}")

    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


def lire_premières_lignes(nom_fichier,n):
    """Lire les n premières lignes d'un fichier"""
    try:
        with open(nom_fichier,'r',encoding='utf-8') as fichier:
            for _ in range(n):
                ligne = fichier.readline()
                if not ligne:
                    break
                print(ligne.strip())
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite :{e}")



def lire_dernières_lignes(nom_fichier, n):
    """Lire les n dernières lignes d'un fichier."""
    try:
        with open(nom_fichier,'r',encoding='utf-8') as fichier:
            lignes = fichier.readlines()
            for ligne in lignes[-n:]:
                print(ligne.strip())
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite :{e}")



def compter_mots(nom_fichier):
    """ Comptage des mots dans un fichier"""

    try:
        with open(nom_fichier,'r',encoding='utf-8') as fichier:
            contenu = fichier.read()
            mots = contenu.split()
            nombre_mots = len(mots)
            print(f"Le fichier {nom_fichier} contient {nombre_mots} mots.")
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")



#Menu intéractif pour permettre à l'utilisateur de choisir
nom_du_fichier = input("Entrer le nom du fichier :")

while True:
    print("\nOptions disponibles :")
    print("1. Lire le fichier en entier")
    print("2. Lire les n premières lignes.")
    print("3. Lire les n dernières lignes.")
    print("4. Compmter le nombre de mots contenus dans le texte.")
    print("5. Quitter.")

    choix = input("Choisissez une option de 1 à 5 :")

    if choix == '1':
        lire_fichier_entier(nom_du_fichier)
    
    elif choix =='2':
        n = int(input("Entrer le nombre n de premières lignes à lire:"))
        lire_premières_lignes(nom_du_fichier,n)

    elif choix =='3':
        n = int(input("Entrer le nombre n de dernières lignes à lire :"))
        lire_dernières_lignes(nom_du_fichier,n)

    elif choix=='4':
        compter_mots(nom_du_fichier)

    elif choix == 5:
        print("Fin du programme.")
        break

    else:
        print("Option invalide, choisir un chiffre entre 1 et 5.")