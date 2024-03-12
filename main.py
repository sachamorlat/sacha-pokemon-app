from classes import *
from rich.console import Console
import json


def charger_pokemons_depuis_json(nom_fichier):
    pokemons = []
    with open(nom_fichier, "r") as fichier:
        donnees = json.load(fichier)
        for pokemon_data in donnees:
            pokemon = Pokemon()
            pokemon.nom = pokemon_data["nom"]
            pokemon.type1 = pokemon_data["type1"]
            pokemon.point_de_vie = pokemon_data["point_de_vie"]
            pokemon.niveau = pokemon_data["niveau"]
            pokemons.append(pokemon)
    return pokemons


# Utilisation de la fonction pour charger les Pokémon depuis le fichier JSON
pokemons_disponibles = charger_pokemons_depuis_json("pokemon.json")

# Affichage des Pokémon chargés
for pokemon in pokemons_disponibles:
    print(
        f"Nom: {pokemon.nom}, Type: {pokemon.type1}, PV: {pokemon.point_de_vie}, Niveau: {pokemon.niveau}"
    )


def main():
    console = Console()

    # Création d'un jeu
    jeu = Jeu()

    # Ajout de joueurs
    joueur1 = Joueur()
    joueur1.nom = input("Joueur 1, veuillez saisir votre nom : ")
    joueur2 = Joueur()
    joueur2.nom = input("Joueur 2, veuillez saisir votre nom : ")
    jeu.joueurs.append(joueur1)
    jeu.joueurs.append(joueur2)

    # Affichage des joueurs
    console.print("Liste des joueurs :")
    for joueur in jeu.joueurs:
        joueur.afficher()

    # Création de Pokémon disponibles
    # pikachu = Pokemon()
    # pikachu.nom = "Pikachu"
    # pikachu.type1 = "Electrique"
    # pikachu.point_de_vie = 100
    # pikachu.niveau = 10

    # mewtwo = Pokemon()
    # mewtwo.nom = "Mewtwo"
    # mewtwo.type1 = "Psy"
    # mewtwo.point_de_vie = 150
    # mewtwo.niveau = 20

    # pokemons_disponibles = [pikachu, mewtwo]

    # Les joueurs choisissent leurs Pokémon
    for joueur in jeu.joueurs:
        console.print(f"\n{joueur.nom}, choisissez vos Pokémon :")
        for i, pokemon in enumerate(pokemons_disponibles, start=1):
            console.print(f"{i}. {pokemon.nom}")
        choix_pokemon = int(
            input("Choisissez le numéro du Pokémon à ajouter à votre équipe : ")
        )
        if choix_pokemon < 1 or choix_pokemon > len(pokemons_disponibles):
            console.print(
                "Choix invalide. Choisissez un numéro parmi les options disponibles."
            )
            continue
        pokemon_choisi = pokemons_disponibles[choix_pokemon - 1]
        joueur.ajouter_pokemon(pokemon_choisi)

    # Affichage des Pokémon des joueurs
    console.print("\nPokémon des joueurs :")
    for joueur in jeu.joueurs:
        joueur.afficher_pokemons()

    # Début du jeu
    console.print("\nDébut du jeu :")
    jeu.jouer()


if __name__ == "__main__":
    main()
