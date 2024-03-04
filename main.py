from classes import *

def main():
    # Création d'un jeu
    jeu = Jeu()

    # Ajout de joueurs
    joueur1 = Joueur()
    joueur1.nom = "Joueur 1"
    joueur2 = Joueur()
    joueur2.nom = "Joueur 2"
    jeu.joueurs.append(joueur1)
    jeu.joueurs.append(joueur2)

    # Affichage des joueurs
    print("Liste des joueurs :")
    for joueur in jeu.joueurs:
        joueur.afficher()

    # Création de Pokémon
    pikachu = Pokemon()
    pikachu.nom = "Pikachu"
    pikachu.type1 = "Electrique"
    pikachu.point_de_vie = 100
    pikachu.niveau = 10

    mewtwo = Pokemon()
    mewtwo.nom = "Mewtwo"
    mewtwo.type1 = "Psy"
    mewtwo.point_de_vie = 150
    mewtwo.niveau = 20

    # Ajout de Pokémon aux joueurs
    joueur1.pokemons.append(pikachu)
    joueur2.pokemons.append(mewtwo)

    # Affichage des Pokémon des joueurs
    print("\nPokémon des joueurs :")
    for joueur in jeu.joueurs:
        joueur.afficher_pokemons()

    # Début du jeu
    print("\nDébut du jeu :")
    jeu.jouer()

if __name__ == "__main__":
    main()
