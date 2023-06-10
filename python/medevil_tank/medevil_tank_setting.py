import pygame

Level_map =[
    '                      ',
    '                      ',
    '                      ',
    '                      ',
    '     XX               ',
    'XP   XX               ',
    'XX                    ',
    'XXXXXXXXXXXXXXXXXXXXXX']


tile_size = 80

gravity = pygame.math.Vector2(0,700)

screen_width = 1000
screen_hight = len(Level_map)*tile_size#412