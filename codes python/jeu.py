import random

nombre_mystère = random.randint(1,100)
   
print("Jeu devinette")
print("Trouve un nombre entre 1 et 100")

while True:
    devinette = int(input("Entre ton choix: "))

    if devinette == nombre_mystère:
        print("Bravo, vous avez deviné le nombre caché.")
        break
    
    elif devinette > nombre_mystère:
        print("Trop élevé.... Essayez encore.")
    
    else:
        print("Trop bas.... Essayez encore.")
