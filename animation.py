import pygame

# Définir une classe qui s'occupera des animations


class AnimateSprite(pygame.sprite.Sprite):

    # Définir les choses à faire à la création de l'entité
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')

    # Définir une  méthode pour animer le sprite
        self.current_image = 0      # Commencer l'image à 0
        self.images = animation.get(sprite_name)
        self.animation = False

    # Définir une méthode pour démarrer l'animation
    def start_animation(self):
        self.animation = True

    # Définir une fonction qui animera le sprite
    def animate(self, loop=False):
        # Vérifier si l'animation est active
        if self.animation:

            # Passer à l'image suivante
            self.current_image += 1

            # Vérifier si on atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # Remettre l'animation au départ
                self.current_image = 0
                # Vérifier si l'animn'est pas en mode boucle
            if loop is False:
                # Desactivation de l'animation
                self.animation = False

            # Modifier l'image précédente par la suivante
            self.image = self.images[self.current_image]


# Définir une fonction pour charger les images d'un sprite

def load_animation_images(sprite_name):
    # Charger les 24 images du sprite du dossier correspondant
    images = []
    # Recuperer le chemin du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"
    # Boucler sur chaque image du dossier
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    # Renvoyer le contenu de la liste d'images
    return images


# Définir un dictionnaire qui va contenir les images chargés de chaque sprite
animation = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player')
}
