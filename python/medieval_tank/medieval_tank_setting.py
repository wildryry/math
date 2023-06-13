import pygame

Level_map =[
    
    
    '                                                                                                                        ',
    '                                                                                                                        ',
    '                                                                                                                        ',
    '                         XXXXX              E                                                                           ',
    '      XX                 B   B            XXXXX                                                                         ',
    '     XX                  X P X            B   B                                                                         ',
    '    XX                   B   B            XXGXX                                                                         ',
    '    XX             X    XXGGGXX         XXBBGBBXX                                                                       ',
    '   XXX             X    B     B       XXBBBBBBBBBXX                                          X                          ',
    '  XXXXX       XX   X    B     B         B   B   B          X    X                           XX                          ',
    ' XXXXXXX      BB   X    XXXXXXX   XXXXXXXXXXXXXXXXX        X    X                           BB                          ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']


tile_size = 80

#for arrows
gravity = pygame.math.Vector2(0,700)

screen_width = 1500#len(Level_map[0])*tile_size
screen_hight = len(Level_map)*tile_size#412
