# Fichier de classes
import json
from rich import print
from rich.console import Console
from rich.table import Table
from rich import color

console = Console()

class Jeu:
    def __init__(self) -> None:
        self.joueurs: list[Joueur] = []

    def charger_pokemons_depuis_json(self, nom_fichier: str):
        pokemons = []
        with open(nom_fichier, "r") as fichier:
            donnees = json.load(fichier)
            for pokemon_data in donnees:
                pokemon = Pokemon()
                pokemon.nom = pokemon_data["nom"]
                pokemon.type1 = pokemon_data["type1"]
                pokemon.point_de_vie = pokemon_data["point_de_vie"]
                pokemon.niveau = pokemon_data["niveau"]
                pokemon.attaques = [Attaque(**attaque_data) for attaque_data in pokemon_data["attaques"]]
                pokemons.append(pokemon)
        return pokemons



    def jouer(self):
        pokemons_disponibles = self.charger_pokemons_depuis_json("pokemon.json")

        for i in range(2):
            nom_joueur = input(f"Joueur {i+1} veuillez saisir votre nom : ")
            joueur = Joueur(nom_joueur)
            self.joueurs.append(joueur)

        joueur_actuel_index = 0  # Pour suivre l'index du joueur actuel

        for _ in range(6):  # Chaque joueur choisit 3 Pokémon
            joueur_actuel = self.joueurs[joueur_actuel_index]
            console.print(f"C'est au tour de [bold]{joueur_actuel.nom}[/bold] de choisir un Pokémon.")
            console.print("Voici la liste des Pokémon disponibles :")
            for i, pokemon in enumerate(pokemons_disponibles, start=1):
                console.print(f"{i}. [green]{pokemon.nom}[/green]")
            choix_pokemon = int(input(f"{joueur_actuel.nom} choisissez un Pokémon : "))
            if choix_pokemon < 1 or choix_pokemon > len(pokemons_disponibles):
                console.print("[red]Choix invalide. Veuillez choisir à nouveau.[/red]")
                continue
            pokemon_choisi = pokemons_disponibles.pop(choix_pokemon - 1)  # Retirer le Pokémon choisi de la liste
            joueur_actuel.ajouter_pokemon(pokemon_choisi)

            # Passer au joueur suivant
            joueur_actuel_index = (joueur_actuel_index + 1) % 2

        for joueur in self.joueurs:
            console.print(f"\nEquipe de [bold]{joueur.nom}[/bold] : \n")
            joueur.afficher_pokemons()

        console.print("\nQue le combat commence !")

        vainqueur = self.combattre()

        console.print(f"Le vainqueur est [bold]{vainqueur.nom}[/bold] !")

        rejouer = input("Voulez-vous rejouer ? (oui/non) ")
        if rejouer.lower() == "oui":
            self.jouer()
        else:
            console.print("Merci d'avoir joué !")
  

    def combattre(self):
        # Déroulement des rounds
        for round in range(7):
            console.print(f"\nRound {round+1} commence !")
            # Combat entre les Pokémons des joueurs
            for i in range(len(self.joueurs)):
                joueur_actuel = self.joueurs[i]
                joueur_oppose = self.joueurs[(i + 1) % 2]  # Pour alterner entre les joueurs
                
                console.print(f"[bold]{joueur_actuel.nom}[/bold], voici les Pokémon disponibles pour le combat :")
                joueur_actuel.afficher_pokemons()            
                pokemon_joueur_actuel = joueur_actuel.recuperer_pokemon(int(input(f"{joueur_actuel.nom} Veuillez choisir un Pokemon ")))  # Premier Pokémon du joueur actuel
                console.print(f"[bold]{joueur_oppose.nom}[/bold], voici les Pokémon disponibles pour le combat :")
                joueur_oppose.afficher_pokemons()  
                pokemon_joueur_oppose = joueur_oppose.recuperer_pokemon(int(input(f"{joueur_oppose.nom} Veuillez choisir un Pokemon ")))  # Premier Pokémon du joueur opposé

                # Logique pour le combat entre les deux Pokémon
                while not (pokemon_joueur_actuel.est_ko() or pokemon_joueur_oppose.est_ko()):
                    # Attaque du Pokémon actuel sur le Pokémon opposé
                    attaque_joueur_actuel = joueur_actuel.choisir_attaque(pokemon_joueur_actuel)
                    pokemon_joueur_actuel.attaquer(pokemon_joueur_oppose, attaque_joueur_actuel)
                    # Vérification si le Pokémon opposé est KO après l'attaque
                    if pokemon_joueur_oppose.est_ko():
                        console.print(f"{pokemon_joueur_oppose.nom} de {joueur_oppose.nom} est K.O. !")
                        # console.print(f"[bold]{joueur_oppose.nom}[/bold], voici les Pokémon disponibles pour le combat :")
                        # joueur_oppose.afficher_pokemons()                          
                        # joueur_oppose.recuperer_pokemon(int(input(f"{joueur_oppose.nom} veuillez choisir un Pokemon ")))
                        break

                    # Attaque du Pokémon opposé sur le Pokémon actuel
                    attaque_joueur_oppose = joueur_oppose.choisir_attaque(pokemon_joueur_oppose)
                    pokemon_joueur_oppose.attaquer(pokemon_joueur_actuel, attaque_joueur_oppose)
                    # Vérification si le Pokémon actuel est KO après l'attaque
                    if pokemon_joueur_actuel.est_ko():
                        console.print(f"{pokemon_joueur_actuel.nom} de {joueur_actuel.nom} est K.O. !")
                        # console.print(f"[bold]{joueur_actuel.nom}[/bold], voici les Pokémon disponibles pour le combat :")
                        # joueur_actuel.afficher_pokemons()                         
                        # joueur_actuel.recuperer_pokemon(int(input(f"{joueur_actuel.nom} veuillez choisir un Pokemon ")))
                        break
                        

            # Vérification si un joueur n'a plus de Pokémon en état de combattre après le round
            if joueur_actuel.pokemons[0].est_ko():
                console.print(f"{joueur_actuel.nom} n'a plus de Pokémon en état de combattre !")
                return joueur_oppose
            elif joueur_oppose.pokemons[0].est_ko():
                console.print(f"{joueur_oppose.nom} n'a plus de Pokémon en état de combattre !")
                return joueur_actuel

        # Si aucun joueur n'a remporté deux manches, déterminez le vainqueur en fonction des points de vie restants
        score_joueur1 = sum([pokemon.point_de_vie for pokemon in self.joueurs[0].pokemons])
        score_joueur2 = sum([pokemon.point_de_vie for pokemon in self.joueurs[1].pokemons])

        if score_joueur1 > score_joueur2:
            return self.joueurs[0]
        elif score_joueur2 > score_joueur1:
            return self.joueurs[1]
        else:
            return None  # Match nul


class Joueur:
    # initialisation liste de pokemon vide
    def __init__(self, nom: str) -> None:
        self.nom: str = nom
        self.manche_gagnee: int = 0
        self.argent: int = 0
        self.pokemons: list[Pokemon] = []

    def ajouter_pokemon(self, pokemon):
        if len(self.pokemons) < 3:
            self.pokemons.append(pokemon)
            console.print(f"{pokemon.nom} a bien été ajouté à l'équipe de [bold]{self.nom}[/bold] !")
        else:
            console.print("[red]Vous avez déjà trois Pokémon dans votre équipe ![/red]")

    def choisir_attaque(self, pokemon):
        console.print(f"Choisissez une attaque pour [green]{pokemon.nom}[/green] :")
        pokemon.afficher_attaques()
        choix = input("Veuillez choisir une attaque en indiquant son numéro : ")
        # Gérer les cas où l'utilisateur ne saisit pas un numéro valide ou une autre entrée non valide
        try:
            choix = int(choix)
            if choix < 1 or choix > len(pokemon.attaques):
                raise ValueError
            attaque_choisie = pokemon.attaques[choix - 1]
            return attaque_choisie
        except ValueError:
            console.print("[red]Veuillez saisir un numéro valide.[/red]")
            return None

    def recuperer_pokemon(self, numero_pokemon: int):
        if numero_pokemon < 1 or numero_pokemon > len(self.pokemons):
            console.print("[red]Numéro de Pokémon invalide.[/red]")
            return self.recuperer_pokemon()
        else:
            pokemon_recupere = self.pokemons[numero_pokemon - 1]
            console.print(f"{pokemon_recupere.nom} est envoyé au combat !\n")
            return pokemon_recupere

    def afficher_pokemons(self):
        if len(self.pokemons) > 0:
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Nom")
            table.add_column("Type")
            table.add_column("PV")
            table.add_column("Niveau")
            for pokemon in self.pokemons:
                if pokemon.est_ko():
                    self.pokemons.remove(pokemon)
                else:
                    nom_colore = self.get_color_by_type(pokemon.type1, pokemon.nom)
                    type1_colore = self.get_color_by_type(pokemon.type1, pokemon.type1)
                    type2_colore = self.get_color_by_type(pokemon.type2, pokemon.type2) if pokemon.type2 else ""
                    table.add_row(
                        nom_colore, f"{type1_colore} {type2_colore}", f"[green]{pokemon.point_de_vie}[/green]", str(pokemon.niveau)
                    )
            console.print(table)
        else:
            console.print(f"[italic]{self.nom} ne possède pas de Pokémon.[/italic]")

    def get_color_by_type(self, type_name: str, text: str) -> str:
        color_map = {
            "Feu": "red",
            "Eau": "blue",
            "Plante": "green",
            "Electrique": "yellow",
            "Psy": "magenta",
            "Fee": "pink",
            "Sol": "brown",                    
            "Insecte": "lightgreen",
            "Normal": "grey",
            "Combat": "orange",
            "Poison": "purple"
            }
        return f"[{color_map.get(type_name, 'white')}] {text} [/{color_map.get(type_name, 'white')}]"

    def afficher(self):
        console.print(
            f"Informations de [bold]{self.nom}[/bold] : \n Manche gagnée : {self.manche_gagnee} \n Argent : {self.argent} \n"
        )


class Pokemon:
    # initialiser la liste d'attaque vide
    def __init__(self) -> None:
        self.nom: str = ""
        self.prix: int = 1
        self.type1: str = ""
        self.type2: str = ""
        self.point_de_vie: int = 1
        self.niveau: int = 1
        self.attaque: int = 1
        self.attaque_speciale: int = 1
        self.defense: int = 1
        self.defense_speciale: int = 1
        self.vitesse: int = 1
        self.attaques: list[Attaque] = []

    def ajouter_attaque(self, attaque):
        if len(self.attaques) <= 4:
            self.attaques.append(attaque)
            console.print(
                f"L'attaque [cyan]{attaque.nom}[/cyan] a bien été ajoutée aux attaques de {self.nom}"
            )
        else:
            console.print(
                f"{self.nom} possède déjà le nombre d'attaque maximal. Veuillez oublier une capacité pour lui en apprendre une autre."
            )

    def oublier_attaque(self, attaque):
        if self.attaques.__contains__(attaque):
            self.attaques.remove(attaque)
            console.print(f"{self.nom} a bien oublié l'attaque [cyan]{attaque.nom}[/cyan]")
        else:
            console.print(f"{self.nom} ne possède pas l'attaque [cyan]{attaque.nom}[/cyan]")

    def attaquer(self, pokemon_cible, attaque):
        degats = attaque.calculer_degats(self, pokemon_cible)
        if degats > 0:
            pokemon_cible.point_de_vie -= degats
            console.print(f"[bold]{self.nom}[/bold] utilise [cyan]{attaque.nom}[/cyan] !")
            console.print(f"[cyan]{attaque.nom}[/cyan] inflige {degats} dégâts à [bold]{pokemon_cible.nom}[/bold] !")
            if pokemon_cible.est_ko():
                console.print(f"[bold]{pokemon_cible.nom}[/bold] est K.O. !")
            else:
                console.print(f"[bold]{pokemon_cible.nom}[/bold] a maintenant {pokemon_cible.point_de_vie} points de vie.")
        else:
            console.print(f"L'attaque [cyan]{attaque.nom}[/cyan] a échoué !")

    def est_ko(self) -> bool:
        if self.point_de_vie > 0:
            return False
        else:
            return True

    def afficher_attaques(self):
        if len(self.attaques) > 0:
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Attaque")
            table.add_column("Type")
            table.add_column("PP")
            table.add_column("Catégorie")
            for attaque in self.attaques:
                table.add_row(attaque.nom, attaque.type, str(attaque.pp), attaque.categorie_attaque)
            console.print(table)
        else:
            console.print(f"[italic]{self.nom} ne possède aucune attaque.[/italic]")

    def afficher(self):
        console.print(
            f"Caractéristique de [bold]{self.nom}[/bold] : \n Pokémon de type {self.type1} {self.type2} \n PV : {self.point_de_vie} \n Niveau {self.niveau} \n"
        )

    def afficher_couleur(self):
        nom_colore = Joueur.get_color_by_type(self.type1).apply(self.nom)
        console.print(
            f"Nom : {nom_colore}, Type : {self.type1} {self.type2}, PV : {self.point_de_vie}, Niveau {self.niveau}"
        )


class Attaque:
    def __init__(self, nom, type, categorie_attaque, precision, puissance, pp) -> None:
        self.nom: str = nom
        self.type: str = type
        self.categorie_attaque: str = categorie_attaque
        self.precision: int = precision
        self.puissance: int = puissance
        self.pp: int = pp

    def calculer_degats(self, pokemon_attaquant: Pokemon, pokemon_cible: Pokemon ) -> int:
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
                console.print("[red]L'attaque de caractéristique doit être physique ou spéciale.[/red]")
        else:
            console.print("[red]Un des pokemon fourni n'existe pas[/red]")

        # Pour gérer le STAB
        if pokemon_attaquant.type1 == self.type or pokemon_attaquant.type2 == self.type:
            degats = int(degats) * 1.5

        # TODO Faire en sorte de gérer la table des types

        return degats
