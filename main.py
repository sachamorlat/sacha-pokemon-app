from classes import *
from rich.console import Console


def main():
    console = Console()

    # Création d'un jeu
    jeu = Jeu()

    # Début du jeu
    jeu.jouer()


if __name__ == "__main__":
    main()
