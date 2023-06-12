import pygame

from medieval_tank_setting import *


class Enemey(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('images/medieval_tank_enemey.png')
        self.image = pygame.transform.scale_by(self.image, 4)
        self.rect = self.image.get_rect(topleft = pos)
        

    def update(self, x_shift, display_surface):
        
        self.rect.x += x_shift
        pygame.draw.rect(display_surface, 'RED', self.rect, width = 5)
        
        
