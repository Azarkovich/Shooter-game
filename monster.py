import pygame
import random
import animation


class Monster(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("mummy")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 2)
        self.start_animation()

    def damage(self, amount):
        # Infliger des dégats
        self.health -= amount

        # Vérifier si son nouveau nombre de PV est <= 0
        if self.health <= 0:
            # Réapparaître comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health

        # Vérifier si la barre d'event est full
        if self.game.comet_event.is_full_loaded():
            # Retirer du jeu
            self.game.all_monsters.remove(self)

            # Appel de méthode pour essayer de déclencher la pluie de comète
            self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def health_bar(self, surface):
        # Définir une couleur pour la jauge de vie (Vert)
        bar_color = (73, 244, 56)

        # Définir une couleur et la position pour l'arrière plan de la jauge (Gris foncé)
        back_bar_color = (52, 53, 52)
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        # Définir la position, la largeur et l'épaisseur de la jauge de vie
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]

        # Déssiner la barre de vie et la barre d'arrière plan
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

        """

    def forward(self):
        # Le déplacement ne se fait que s'il n'y a pas de collisions avec un groupe de joueurs
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # Si le monstre est en collision avec le joueur
        else:
            #Infliger des dégats
            self.game.player.damage(self.attack)
            print("L'ennemi attaque")

        """

    def forward(self):
        if self.game.check_collision(self, self.game.all_players):
            self.game.player.damage(self.attack)
        else:
            self.rect.x -= self.velocity
