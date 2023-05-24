

import pygame

import sys


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('images/stick_man.png')
        self.rect = self.image.get_rect(center = (x,y))
        self.rect.x = x
        self.rect.y = y

    def update(self):

        None

    def draw(self, surface):
        surface.blit(self.image , self.rect)
        None


class Arrow(pygame.sprite.Sprite):    
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('images/arrow.png')
        self.rect = self.image.get_rect(center = (x,y))
        self.rect.x = x
        self.rect.y = y
        None

    def update(self):
        None

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


def add_arrow(amount , x , y):
    
    for i in range(amount):
        new_arrow = Arrow(x, y + ((i-1)*-25))
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
add_arrow(1,300,100)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('pog')
            None


    screen.fill((3, 77, 61))
    arrow_group.draw(screen)
    player_group.draw(screen)
    

    


    

    pygame.display.flip()
    clock.tick(60)


