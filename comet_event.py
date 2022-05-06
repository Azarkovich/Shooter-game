import pygame
from comet import Comet

# Créer une classe pour gérer l'évènement


class CometFallEvent:

    # Lors du chargement -> Créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 15
        self.game = game
        self.fall_mode = False

        # Définir un groupe de sprite pour stocker les cometes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def comet_fall(self):
        # Boucle pour les valeurs entre 1 et 10
        for i in range(1, 10):
            # Apparaître 1 première boule de feu
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # La jauge d'event est totallement full et qu'il n'y a pas de monstres
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("Il pleut du feu !!!!!")
            self.comet_fall()
            self.fall_mode = True   # Activer l'évènement

    def update_bar(self, surface):
        # Ajouter du pourcentage à la barre
        self.add_percent()

        # La barre d'arrière plan
        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # L'axe des X
            surface.get_height() - 20,   # L'axe des Y
            surface.get_width(),    # Longueur de la fenêtre
            10  # Epaisseur de la barre
        ])
        # Barre rouge = jauge d'event
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # L'axe des X
            surface.get_height() - 20,  # L'axe des Y
            (surface.get_width() / 100) * self.percent,  # Longueur de la fenêtre
            10  # Epaisseur de la barre
        ])

