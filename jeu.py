import random
def jouer_jeu():
    nombre_mystère = random.randint(1,100)
    tentative = 0
    print("Jeu devinette")
    print("Trouve un nombre entre 1 et 100")

    while True:
        tentative += 1
        devinette = int(input("entre ton choix"))
        if devinette < nombre_mystère :
            print("trop bas .... essayez encore")
        elif devinette > nombre_mystère :
            print("trop élevé .... essayez encore")
        else:
            print("bravo, vous avez deviné le nombre caché")
        break

if __name__== "__main__" :
    jouer_jeu()