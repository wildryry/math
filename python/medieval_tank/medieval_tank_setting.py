import pygame

pygame.display.set_caption('medieval_tank')

Level_map =[
    
    
    '                                                                                                                        ',
    '                                                                                                                        ',
    '                           P                                                                                            ',
    '                         XXXXX              E                                                                           ',
    '      XX                 B   B            XXXXX                                                                         ',
    '     XX                  X   X            B   B                                          XXXX                           ',
    '    XX                   B   B            XXGXX                                         B    B                          ',
    '    XX             X    XXGGGXX         XXBBGBBXX       G                               X    X                          ',
    '   XXX             X    B     B       XXBBBBBBBBBXX     G                  EEE          X    X                          ',
    '  XXXXX       XX   X    B     B         B   B   B          X    X          EEE          XXBBXX                          ',
    ' XXXXXXX      BB   X    XXXXXXX   XXXXXXXXXXXXXXXXX        X    X          EEE          BB  BB                          ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']


tile_size = 80

#for arrows
gravity = pygame.math.Vector2(0,700)

screen_width = 1500#len(Level_map[0])*tile_size
screen_hight = len(Level_map)*tile_size#412
