import pygame

Level_map =[
    
    
    '                                                      ',
    '                                                      ',
    '                                                      ',
    '                         XXXXX                        ',
    '    XXXX                 B   B            XXXXX       ',
    '    XXX                  X   X            B   B       ',
    '    XX                   B E B            XXGXX       ',
    '    XX             X    XXGGGXX         XXBBGBBXX     ',
    '   XXX        P    X    B     B       XXBBBBBBBBBXX   ',
    '  XXXXX       XX   X    B     B         B   B   B     ',
    ' XXXXXXX      BB   X    XXXXXXX   XXXXXXXXXXXXXXXXX   ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']


tile_size = 80

#for arrows
gravity = pygame.math.Vector2(0,700)

screen_width = 1500#len(Level_map[0])*tile_size
screen_hight = len(Level_map)*tile_size#412
