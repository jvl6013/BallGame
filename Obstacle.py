import pygame;

GRAY = [170, 170, 170]

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
