class Banque:
    def __init__(self, solde):
        self.solde = solde

    def depot(self, montant):
        self.solde += montant
        return self.solde
    
    def retrait(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            return self.solde
    
        else:
            print("Fonds insuffisants. Retrait impossible.")
            return self.solde