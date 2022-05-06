import pygame
from game import Game
from projectile import Projectile
pygame.init()


# Générer la fenêtre du jeu
pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1080, 720))  # Renvoie une surface

# Importer l'arrière plan du jeu
background = pygame.image.load('assets/bg.jpg')

# Importer la bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width() / 4
# banner_rect.x = math.ceil(screen.get_width() /4 à utiliser avec la bibliothèque math

# Importer un bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width() / 3.33
play_button_rect.y = screen.get_height() / 2

# Charger le jeu
game = Game()


# Création d'une variable pour maintenir la fenêtre active
running = True

# Boucle tant que cette condition est vraie
while running:

    # Appliquer l'arrière plan du jeu
    screen.blit(background, (0, -200))

    # Vérifier si le jeu à commencer ou non
    if game.is_playing:
        # Déclencher les instructions de la partie
        game.update(screen)
        # Vérifier si le jeu n'a pas commencé
    else:
        # Ajouter l'écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # Mettre à jour l'écran
    pygame.display.flip()

    # Si le joueur ferme la fenêtre
    for event in pygame.event.get():
        # Que l'évènement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture de la fenêtre")

        # Détecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # Détecter si la touche espace est enclenchée pour lancr leprojectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérification si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # Mettre le jeu en mode lancé
                game.start()


