import random

nombre_mystère = random.randint(1,100)
   
print("Jeu devinette")
print("Trouve un nombre entre 1 et 100")

while True:
            
                    devinette = int(input("entre ton choix:"))
                
if devinette == nombre_mystère :
        print("bravo, vous avez deviné le nombre caché")
        break
    
elif devinette > nombre_mystère :
print("trop élevé .... essayez encore")
else:
print("trop bas .... essayez encore")
    

            