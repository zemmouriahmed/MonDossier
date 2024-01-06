# combiner 2 dictionnaires en faisant la somme des valeurs des clés communes

def combidic (dic1,dic2):
    tampon = {}

    # ajouter les valeurs des clés du dic1
    for key, value in dic1.items():
        tampon[key] = value

    # addition des valeurs des clés communes (identiques)
    for key, value in dic2.items():
        if key in tampon:
            tampon[key] += value
        else:
            tampon[key] = value
        
    return tampon

# saisie de dic1 et dic2
dic1_str = input("saisir le premier dictionnaire au format clé:valeur (format de la saisie exemple 'a':11), séparés par des virgules :")
dic2_str = input("saisir le second dictionnaire au format clé:valeur (format de la saisie exemple 'a':11), séparés par des virgules :")

#convertion des chaînes en dictionnaires en utilisant eval
dic1 = eval("{" + dic1_str + "}")
dic2 = eval("{" + dic2_str + "}")

# appeler combidic et afficher le résultat
combinaison_dictionnaires = combidic(dic1, dic2)

print(f"Dictionnaire combiné avec les valeurs additionnées pour les clés communes : {combinaison_dictionnaires}")