

import pygame

import sys

import math as ma

from medieval_tank_setting import *

from medieval_tiles import Tile

from medieval_tank_level import Level

from medieval_tank_player import Player

from medieval_arrow import Arrow


arrow_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()





mouse_x = 0
mouse_y = 0
mouse_down = False




clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width,screen_hight)) 
done = False
level = Level(Level_map,screen)




def sense_key(key):
    keys = pygame.key.get_pressed()
    if keys[key]:
        return True
    else:
        return False
    None



def shoot_arrow(speedorg):
    
    for sprite in level.player:

        player_vector = pygame.math.Vector2(sprite.rect.center)
        arrow_pos = pygame.math.Vector2(sprite.rect.center)

        mouse_vector = pygame.math.Vector2((mouse_x,mouse_y))

        dir = mouse_vector - player_vector
        dir = dir.normalize()

        
        new_vector = pygame.math.Vector2(-15,-30)
        arrow_pos += new_vector


        speed = speedorg * 10
        
        add_arrow(arrow_pos , speed , dir) 
        
   
        


def add_arrow(arrow_pos , speed ,dir):

    

    
    
    
    new_arrow = Arrow(arrow_pos, speed , dir)
    level.arrows.add(new_arrow)
    all_sprites.add(new_arrow)
        
    None
def add_player(amount , x , y):

    for i in range(amount):
        new_player = Player(x, y + ((i-1)*-25))
        player_group.add(new_player)
        all_sprites.add(new_player)
        None







funny = 5

while not done:
    
    

    mouse_x,mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        #if event.type == pygame.MOUSEBUTTONDOWN:
    click = pygame.mouse.get_pressed()
    if click[0] == True:
        shoot_arrow(75)
        mouse_down = True
    else:
        mouse_down = False
                

    
    

    
   

    screen.fill((3, 77, 61))
    arrow_group.draw(screen)
    player_group.draw(screen)
    
    level.run(clock)    
    arrow_group.update(clock.get_time())
    
    
    

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()

