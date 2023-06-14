import pygame

from medieval_tank_setting import *


class Enemey(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('images/medieval_tank_enemey.png')
        self.image = pygame.transform.scale_by(self.image, 4)
        self.rect = self.image.get_rect(topleft = pos)
        self.HP = 3
        
    def hit_check(self, arrows):

        for arrow in arrows.sprites():
            if self.rect.colliderect(arrow) and arrow.stuck == False:
                self.HP += -1
                arrow.kill()
                if self.HP <= 0:
                    self.kill()
            


    def update(self, x_shift, display_surface, arrows):
        self.hit_check(arrows)
        pygame.draw.rect(display_surface, 'RED', self.rect, width = 1)
        self.rect.x += x_shift
        
        
        
