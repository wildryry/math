

import pygame

import sys

screen_width = 1700
screen_hight = 700

clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width,screen_hight)) 

done = False

class Arrow(pygame.sprite.Sprite):    
    def __init__(self,x,y):
        super.__init__()
        self.surface = pygame.image.load('images/arrow.png')
        self.rect = self.surface.get_rect(center = (x,y))
        self.rect.x = x
        self.rect.y = y
        None

    def update(self):
        None

    def draw(self,surface):
        surface.blit(self.surface , self.rect)

new_arrow = Arrow(400,300)
arrow_group = pygame.sprite.Group()
arrow_group.add(new_arrow)



while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    arrow_group.draw

    pygame.display.flip()
    clock.tick(60)


