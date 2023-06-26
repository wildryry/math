import pygame
from medieval_tank_setting import *
from tank_head import Head1


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
        self.image = pygame.image.load('images/tank_sprite1.1.png')
        self.image = pygame.transform.scale_by(self.image, 5)
        self.image_origonal = self.image
        self.rect = self.image.get_rect(center = (x + tile_size * 0.5,y + tile_size * 0.5))
        self.head = pygame.sprite.Group()

        self.pos = pygame.math.Vector2(x,y)
        self.pre_pos = pygame.math.Vector2(x,y)

        head = Head1((self.pos.x,self.pos.y - 30))
        self.head.add(head)

        self.grounded = False
        self.sled = False
        self.vol = pygame.math.Vector2(0,0)
        self.speed = 10
        self.gravity = 0.65
        self.jump_speed = -15
        self.flipped = False

    def get_input(self):

    


        if sense_key(pygame.K_w):
          None  
        
        if sense_key(pygame.K_s):
            
            None
        if self.sled == False:
            if sense_key(pygame.K_a):
                self.vol.x = -1
                self.image = self.image_origonal
                self.flipped = False
                
                None

            elif sense_key(pygame.K_d):
                self.vol.x = 1
                self.image = pygame.transform.flip(self.image_origonal, True, False)
                self.flipped = True
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
        self.head.update(self.rect.center, self.flipped)
        
        
        

    