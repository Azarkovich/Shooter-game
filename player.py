import pygame
from projectile import Projectile
import animation
# Créer une première classe qui représente le joueur


class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 30
        self.velocity = 1.5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def update_animation(self):
        self.animate()

    def damage(self, amount):
        # Infliger des dégats
        if self.health - amount > amount:
            self.health -= amount
            print("Le joueur subit des dégats")
        else:
            # Si le joueur n'a plus e PV
            self.game.game_over()

    def player_health_bar(self, surface):
        # Définir la position des jauges de vies
        """
        player_health_bar_position = [self.rect.x + 50, self.rect.y + 20, self.max_health, 7]
        back_player_health_bar_position = [self.rect.x + 50, self.rect.y + 20, self.max_health, 7]
        """
        # Déssiner les jauges de vie
        pygame.draw.rect(surface, (52, 53, 52), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (73, 244, 56), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])

    def launch_projectile(self):
        # Créer une instance de la classe projectile
        self.all_projectiles.add(Projectile(self))
        # Démarrer l'animation
        self.start_animation()

    def move_right(self):
        # Si le joueur n'est pas ej collision avec un monstre
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
