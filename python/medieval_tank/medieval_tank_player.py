import pygame
from medieval_tank_setting import *


def sense_key(key):
    keys = pygame.key.get_pressed()
    if keys[key]:
        return True
    else:
        return False
    None

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('images/tank_sprite.png')
        self.image_origonal = self.image
        self.rect = self.image.get_rect(center = (x + tile_size * 0.5,y + tile_size * 0.5))

        self.pos = pygame.math.Vector2(x,y)
        self.pre_pos = pygame.math.Vector2(x,y)


        self.grounded = False
        self.vol = pygame.math.Vector2(0,0)
        self.speed = 5
        self.gravity = 0.3
        self.jump_speed = -11

        
    def get_input(self):
        if sense_key(pygame.K_w):
          None  
        
        if sense_key(pygame.K_s):
            
            None
            
        if sense_key(pygame.K_a):
            self.vol.x = -1
            self.image = self.image_origonal
            
            None

        elif sense_key(pygame.K_d):
            self.vol.x = 1
            self.image = pygame.transform.flip(self.image_origonal, True, False)
            None
        else:
            self.vol.x = 0
            None
        if sense_key(pygame.K_SPACE):
            self.jump()


    def apply_gravity(self):
        self.vol.y += self.gravity
        self.rect.y += self.vol.y


    def jump(self):
        if self.grounded:
            self.vol.y = self.jump_speed
            self.grounded = False


    def update(self):
        self.get_input()
        
        None


    def draw(self, surface):
        surface.blit(self.image , self.rect)
        None