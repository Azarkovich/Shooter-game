import pygame
from monster import Monster
from player import Player
from comet_event import CometFallEvent
# Créer une seconde classe qui représente le jeu


class Game:

    def __init__(self):
        # Définir si le jeu à commencer ou non
        self.is_playing = False
        # Générer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # Générer l'event
        self.comet_event = CometFallEvent(self)
        # Définir un groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # Remettre le jeu à zéro, retirer les monstres, remettre les monstres à 100PV, jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.all_projectiles = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False

    def update(self, screen):
        # Appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # Actualiser la barre de vie du joueur
        self.player.player_health_bar(screen)

        # Actualiser l'animation du joueur
        self.player.update_animation()

        # Actualiser la barre d'event du jeu
        self.comet_event.update_bar(screen)

        # Récupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move_forward()

        # Récupérer les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.health_bar(screen)
            monster.update_animation()

        # Récupérer les comètes
        for comet in self.comet_event.all_comets:
            comet.fall()

        # Aplliquer l'ensemble des images du groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # Appliquer l'ensemble des images du groupe de monstre
        self.all_monsters.draw(screen)

        # Appliquer l'ensemble des images du groupe de cometes
        self.comet_event.all_comets.draw(screen)

        # Vérifier si le joueur shouhaite aller à G ou à D
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

