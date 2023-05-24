

import pygame

import sys


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
    def __init__(self,x,y,speed,rotation):
        super().__init__()
        self.image = pygame.image.load('images/arrow.png')
        self.image = pygame.transform.rotate(self.image, rotation)
        self.rect = self.image.get_rect(center = (x,y))
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.rotation = rotation
        None

    def update(self):
        if self.speed > 0 :
            
            self.rect.x += self.speed
        else:
            self.rect.x += self.speed
        
        if self.rect.x > screen_width or self.rect.y > screen_hight:
            self.kill()
        elif self.rect.x < 0 or self.rect.y < 0:
            self.kill()

    def draw(self,surface):
        surface.blit(self.surface , self.rect)


arrow_group = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

player_group = pygame.sprite.Group()

screen_width = 1000
screen_hight = 412

clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width,screen_hight)) 

done = False

def shoot_arrow(speed):
    #add_arrow(1,pygame.mouse.get_pos())
    None


def add_arrow(amount , x , y , speed):

    if speed > 0:
        rotation = 180
    else:
        rotation = 0
    
    for i in range(amount):
        new_arrow = Arrow(x, y + (i-1)*-25,speed , rotation)
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
add_arrow(1,300,100,4)


funny = 5

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                wkey = True
                None


    screen.fill((3, 77, 61))
    arrow_group.draw(screen)
    player_group.draw(screen)
    

    arrow_group.update()

    

    pygame.display.flip()
    clock.tick(60)


