# case_spe.py





# Cette fonction pourrait être utilisée pour initialiser un ensemble de cases spéciales dans tableau.py
def initialiser_cases_speciales( config=None):
    cases_speciales = {}

    if config is None:
        config = { # Configuration par défaut si aucune n'est fournie
            'LettreDouble': [(3, 0), (11, 0), (6, 2), (8, 2), (0, 3), (7, 3), (14, 3), (2, 6), (6, 6), (8, 6), (12, 6), (3, 7), (11, 7), (2, 8), (6, 8), (8, 8), (12, 8), (0, 11), (7, 11), (14, 11), (6, 12), (8, 12), (3, 14), (11, 14)],
            'LettreTriple': [(5, 1), (9, 1), (1, 5), (5, 5), (9, 5), (13, 5), (1, 9), (5, 9), (9, 9), (13, 9), (5, 13), (9, 13)],
            'MotDouble': [(1, 1), (2, 2), (3, 3), (4, 4), (7, 7), (10, 10), (11, 11), (12, 12), (13, 13), (13, 1), (12, 2), (11, 3), (10, 4), (4, 10), (3, 11), (2, 12), (1, 13)],
            'MotTriple': [(0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14)],
        }
        pass

    for type_case, positions in config.items():
        for position in positions :
            x , y = position
            case = CaseSpeciale (x,y, type_case)
            cases_speciales[(x, y)] = (case.couleur, case.inscription)


    return cases_speciales





class CaseSpeciale:
    def __init__(self, x, y, type_case="Normale"):
        self.x = x
        self.y = y
        self.type_case = type_case
        self.couleur, self.inscription = self.definir_proprietes(type_case)

    @staticmethod
    def definir_proprietes(type_case):
        # Associe les caractéristiques à chaque type de case spéciale
        proprietes = {
            'LettreDouble': ('#ADD8E6', 'LD'),
            'LettreTriple': ('#CCFFCC', 'LT'),
            'MotDouble': ('Pink', 'MD'),
            'MotTriple': ('Red', 'MT'),
        }
        return proprietes.get(type_case, ('White', ''))

