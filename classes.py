# Fichier de classes


class Jeu:
    def __init__(self) -> None:
        self.joueurs: list[Joueur] = []

    def jouer(self):
        input("Nouveau Jeu : \n Appuyer sur entrée pour commencer :")


class Joueur:
    # initialisation liste de pokemon vide
    def __init__(self) -> None:
        self.nom: str = ""
        self.manche_gagnee: int = 0
        self.argent: int = 0
        self.pokemons: list[Pokemon] = []

    def choisir_pokemon(self, pokemons_disponibles):
        print(f"Bonjour {self.nom} ! Voici la liste des Pokémon disponibles :")
        for i, pokemon in enumerate(pokemons_disponibles, start=1):
            print(f"{i}. {pokemon.nom}")
        choix = input("Veuillez choisir un Pokémon en indiquant son numéro : ")
        try:
            choix = int(choix)
            if choix < 1 or choix > len(pokemons_disponibles):
                raise ValueError
            pokemon_choisi = pokemons_disponibles[choix - 1]
            self.pokemons.append(pokemon_choisi)
            print(f"{pokemon_choisi.nom} a bien été ajouté à votre équipe !")
        except ValueError:
            print("Veuillez saisir un numéro valide.")

    def ajouter_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{pokemon.nom} a bien été ajouté à votre équipe ! \n")

    def choisir_attaque(self, pokemon):
        print(f"Choisissez une attaque pour {pokemon.nom} :")
        for i, attaque in enumerate(pokemon.attaques, start=1):
            print(f"{i}. {attaque.nom}")
        choix = input("Veuillez choisir une attaque en indiquant son numéro : ")
        # Gérer les cas où l'utilisateur ne saisit pas un numéro valide ou une autre entrée non valide
        try:
            choix = int(choix)
            if choix < 1 or choix > len(pokemon.attaques):
                raise ValueError
            attaque_choisie = pokemon.attaques[choix - 1]
            return attaque_choisie
        except ValueError:
            print("Veuillez saisir un numéro valide.")
            return None

    def recuperer_pokemon(self, numero_pokemon):
        if numero_pokemon < 1 or numero_pokemon > len(self.pokemons):
            print("Numéro de Pokémon invalide.")
            return None
        else:
            pokemon_recupere = self.pokemons[numero_pokemon - 1]
            print(f"{pokemon_recupere.nom} a été récupéré !")
            return pokemon_recupere

    def afficher_pokemons(self):
        if self.pokemons.__len__() > 0:
            for pokemon in self.pokemons:
                print(
                    f"{pokemon.nom}, Type : {pokemon.type1} {pokemon.type2}, PV : {pokemon.point_de_vie}, Niveau {pokemon.niveau}"
                )
        else:
            print(f"{self.nom} ne possède pas de Pokémon.")

    def afficher(self):
        # à voir pour rajouter un if self is not None
        print(
            f"Informations de {self.nom} : \n Manche gagnée : {self.manche_gagnee} \n Argent : {self.argent} \n"
        )


class Pokemon:
    # initialiser la liste d'attaque vide
    def __init__(self) -> None:
        self.nom: str = ""
        self.prix: int = 0
        self.type1: str = ""
        self.type2: str = ""
        self.point_de_vie: int
        self.niveau: int = 1
        self.attaque: int
        self.attaque_speciale: int
        self.defense: int
        self.defense_speciale: int
        self.vitesse: int
        self.attaques: list[Attaque] = []

    def ajouter_attaque(self, attaque):
        if self.attaques.__len__() <= 4:
            self.attaques.append(attaque)
            print(
                f"L'attaque {attaque.nom} a bien été ajoutée aux attaques de {self.nom}"
            )
        else:
            print(
                f"{self.nom} possède déjà le nombre d'attaque maximal. Veuillez oublier une capacité pour lui en apprendre une autre."
            )

    def oublier_attaque(self, attaque):
        if self.attaques.__contains__(attaque):
            self.attaques.remove(attaque)
            print(f"{self.nom} a bien oublié l'attaque {attaque.nom}")
        else:
            print(f"{self.nom} ne possède pas l'attaque {attaque.nom}")

    def attaquer(self, pokemon_cible, attaque):
        # à compléter
        pass

    def est_ko(self) -> bool:
        if self.point_de_vie > 0:
            return False
        else:
            return True

    def afficher_attaques(self):
        if self.attaques.count() > 0:
            for attaque in self.attaques:
                print(
                    f"{attaque.nom}, Type {attaque.type}, PP restant {attaque.pp}, Catégorie {attaque.categorie_attaque}. \n"
                )
        else:
            print(f"{self.nom} ne possède aucune attaque.")

    def afficher(self):
        # à voir pour rajouter un if self is not None
        print(
            f"Caractéristique de {self.nom} : \n Pokémon de type {self.type1} {self.type2} \n PV : {self.point_de_vie} \n Niveau {self.niveau} \n"
        )


class Attaque:
    def __init__(self, nom, type, categorie_attaque, precision, puissance, pp) -> None:
        self.nom: str = nom
        self.type: str = type
        self.categorie_attaque: str = categorie_attaque
        self.precision: int = precision
        self.puissance: int = puissance
        self.pp: int = pp

    def calculer_degats(self, pokemon_attaquant, pokemon_cible) -> int:
        degats: int = 0

        if pokemon_attaquant is not None and pokemon_cible is not None:
            degats = int(
                ((pokemon_attaquant.niveau * 0.4 + 2) * self.puissance)
            )  # Formule de calcul de dégats

            if self.categorie_attaque == "physique":
                degats = int(
                    (
                        ((degats) * pokemon_attaquant.attaque)
                        / (pokemon_cible.defense * 50)
                    )
                    + 2
                )
            elif self.categorie_attaque == "speciale":
                degats = int(
                    (
                        ((degats) * pokemon_attaquant.attaque_speciale)
                        / (pokemon_cible.defense_speciale * 50)
                    )
                    + 2
                )
            else:
                print("L'attaque de caractéristique doit être physique ou spéciale.")
        else:
            print("Un des pokemon fourni n'existe pas")

        # Pour gérer le STAB
        if pokemon_attaquant.type1 == self.type or pokemon_attaquant.type2 == self.type:
            degats = int(degats) * 1.5

        # TODO Faire en sorte de gérer la table des types

        return degats
