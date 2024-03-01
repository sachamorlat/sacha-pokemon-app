# Fichier de classes 

class Jeu:
    def __init__(self) -> None:
        pass



class Joueur:
    # initialisation liste de pokemon vide 
    def __init__(self) -> None:
        self.nom : str = ""
        self.manche_gagnée : int = 0
        self.argent : int = 0
        self.pokemons : list = []

    
    def choisir_pokemon(self):
        pass
        
    def ajouter_pokemon(self):
        pass
    
    def choisir_attaque(self):
        pass
    
    def recuperer_pokemon(self):
        pass
    def afficher_pokemons(self):
        pass
    def afficher(self):
        pass

class Pokemon:
    # initialiser la liste d'attaque vide 
    def __init__(self) -> None:
        self.nom : str = ""
        self.prix : int = 0
        self.type1 : str = ""
        self.type2 : str = ""
        self.point_de_vie : int
        self.niveau : int = 1
        self.attaque : int 
        self.attaque_speciale : int
        self.defense : int 
        self.defense_speciale : int 
        self.vitesse : int 
        self.attaques : list = []

    def ajouter_attaque(self):
        pass
    
    def attaquer(self):
        pass
    
    def est_ko(self):
        pass

    def afficher_attaques(self):
        pass

    def afficher(self):
        pass

class Attaque:
    def __init__(self) -> None:
        self.nom : str
        self.type : str
        self.categorie_attaque : str
        self.precision : int 
        self.puissance : int 
        self.pp : int 

    def calculer_degats(self):
        pass
