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

    def ajouter_attaque(self, attaque):
        if (self.attaques.count() <= 4):
            self.attaques.append(attaque)
            print(f"L'attaque {attaque.nom} a bien été ajoutée aux attaques de {self.nom}")
        else :
            print(f"{self.nom} possède déjà le nombre d'attaque maximal. Veuillez oublier une capacité pour lui en apprendre une autre.")

    def oublier_attaque(self, attaque):
        if self.attaques.__contains__(attaque):
            self.attaques.remove(attaque)
            print(f"{self.nom} a bien oublié l'attaque {attaque.nom}")
        else :
            print(f"{self.nom} ne possède pas l'attaque {attaque.nom}")        
    
    def attaquer(self, pokemon, attaque):
        pass
    
    def est_ko(self) -> bool:
        if self.point_de_vie > 0:
            return False
        else:
            return True 

    def afficher_attaques(self):
        if (self.attaques.count() > 0):
            for attaque in self.attaques:
                print(f"{attaque.nom}, Type {attaque.type}, PP restant {attaque.pp}, Catégorie {attaque.categorie_attaque}. \n")
        else :
            print(f"{self.nom} ne possède aucune attaque.")

    def afficher(self):
        print(f"Caractéristique de {self.nom} : \n Pokémon de type {self.type1} {self.type2} \n PV : {self.point_de_vie} \n Niveau {self.niveau} \n")

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
