def addition(a,b):
    return a+b

def soustraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b != 0 : 
     return a/b
    else:
        print("la division par 0 n'existe pas")

print()
    
N1 = float(input("entrer premier nombre : "))

print()

N2 = float(input("entrer second nombre :"))

print()

Op = input("entrer opération :")

if Op == '+':
            resultat = addition(N1,N2)

elif Op == '*':
            resultat = multiplication(N1,N2)

elif Op == '-' :
            resultat = soustraction(N1,N2)

elif Op == '/' :
            resultat = division(N1,N2)

else :
       print()
       print()
       print("vérifier vos entrées")

print()                    

print(f"{N1} {Op} {N2} = {resultat}")
