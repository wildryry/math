

import pygame

import sys

import math as ma


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('images/tank_sprite.png')
        self.rect = self.image.get_rect(center = (x,y))
        self.rect.x = x
        self.rect.y = y

    def update(self):

        None

    def draw(self, surface):
        surface.blit(self.image , self.rect)
        None


class Arrow(pygame.sprite.Sprite):    
    def __init__(self, x , y , xspeed ,yspeed, rotation):
        super().__init__()
        self.orginal_image = pygame.image.load('images/arrow.png')
        self.image = pygame.transform.rotate(self.orginal_image, rotation)
        self.rect = self.image.get_rect(center = (x,y))

        self.rect.x = x
        self.rect.y = y
        
        self.speedx = xspeed
        self.speedy = yspeed
        
        
        self.rotation = rotation
        None

    def update(self):

        self.speedy += gravity*0.1
        self.rect.y += self.speedy 
        
        if self.speedx > 0 :
            
            
            self.rotation = (ma.degrees(ma.atan(-self.speedy / self.speedx)) + 180)
        else:
            
            self.rotation = ma.degrees(ma.atan(-self.speedy / self.speedx))

        self.rect.x += self.speedx
        self.image = pygame.transform.rotate(self.orginal_image, self.rotation)
        
        
        
        if self.rect.x > screen_width or self.rect.y > screen_hight:
            self.kill()
        elif self.rect.x < -75 or self.rect.y < -75:
            self.kill()

        

        

    def draw(self,surface):
        surface.blit(self.surface , self.rect)


arrow_group = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

player_group = pygame.sprite.Group()

screen_width = 1000
screen_hight = 412

gravity = 0.5

mouse_x = 0

mouse_y = 0

akey = False

dkey = False

clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width,screen_hight)) 

done = False

def shoot_arrow(speed,dir):
    for sprite in player_group:
        add_arrow(1 , sprite.rect.x + 10 , sprite.rect.y - 20 , speed , dir) 
   
        


def add_arrow(amount , x , y , xspeed ,dir):

    yspeed = ma.tan(dir)#/xspeed
    xspeed = xspeed - yspeed


    if xspeed > 0:
        rotation = 180
    else:
        rotation = 0

    
    
    for i in range(amount):
        new_arrow = Arrow(x, y + (i-1)*-25 , xspeed , yspeed , rotation)
        arrow_group.add(new_arrow)
        all_sprites.add(new_arrow)
        None
def add_player(amount , x , y):

    for i in range(amount):
        new_player = Player(x, y + ((i-1)*-25))
        player_group.add(new_player)
        all_sprites.add(new_player)
        None
add_player(1, 500, 100)
add_player(1, 500, 250)



funny = 5

while not done:
    mouse_x,mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                wkey = True
                shoot_arrow(-15,0)
                None
            
            if event.key == pygame.K_s:
                skey = True
                shoot_arrow(15,0)
                None

            if event.key == pygame.K_SPACE:
                spaceKey = True
                for sprite in player_group:
                    shoot_arrow(-15,ma.degrees(ma.atan((sprite.rect.y - mouse_y) / (sprite.rect.x - mouse_x))))
                

            if event.key == pygame.K_a:
                akey = True
                for sprite in player_group:
                    sprite.rect.x += -sprite.image.get_width()
                    None
            

            if event.key == pygame.K_d:
                dkey = True
                for sprite in player_group:
                    sprite.rect.x += sprite.image.get_width()
                None
            
                
        else:
            skey = False
            dkey = False
            akey = False
            wkey = False
            spacekey = False


    

    screen.fill((3, 77, 61))
    arrow_group.draw(screen)
    player_group.draw(screen)
    

    arrow_group.update()

    

    pygame.display.flip()
    clock.tick(60)


