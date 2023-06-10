import pygame
from medevil_tank_setting import *


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('images/tank_sprite.png')
        self.rect = self.image.get_rect(center = (x,y))

        self.pos = pygame.math.Vector2(x,y)

        self.vol = pygame.math.Vector2(0,0)

        self.pre_pos = pygame.math.Vector2(x,y)

        self.rect.x = x
        self.rect.y = y

    def update(self,delta_time):

        
        

        self.pre_pos = self.pos

        self.pos += self.vol * delta_time/1000

        self.vol += gravity * delta_time/1000
        
        

        
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        None


        
        
        #'''

    def draw(self, surface):
        surface.blit(self.image , self.rect)
        None