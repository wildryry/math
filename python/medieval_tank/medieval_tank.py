

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

        
    
    
    
        
    None
def add_player(amount , x , y):

    for i in range(amount):
        new_player = Player(x, y + ((i-1)*-25))
        player_group.add(new_player)
        all_sprites.add(new_player)
        None



while not done:
    
    

    mouse_x,mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        
                

    screen.fill((3, 77, 61))
    level.run(clock)   
     

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()

