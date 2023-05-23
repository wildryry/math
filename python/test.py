

import pygame

import sys


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

screen_width = 1700
screen_hight = 700

clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width,screen_hight)) 

done = False


def add_arrow(amount):
    
    for i in range(amount):
        new_arrow = Arrow(300, 400 + ((i-1)*-25))
        arrow_group.add(new_arrow)
        None

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill((3, 77, 61))
    arrow_group.draw(screen)

    add_arrow(1)


    

    pygame.display.flip()
    clock.tick(60)


