import pygame

Level_map =[
    '                                               ',
    '    XXXX                                       ',
    '    XXX                  XXXXX                 ',
    '    XX        P          B   B            XXGXX',
    '    XX             X    XXGGGXX         XXBBGBBXX',
    '   XXX             X    B     B       XXBBBBBBBBBXX',
    '  XXXXX       XX   X    B     B         B   B   B',
    ' XXXXXXX      BB   X    XXXXXXX   XXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']


tile_size = 82

#for arrows
gravity = pygame.math.Vector2(0,700)

screen_width = 1500#len(Level_map[0])*tile_size
screen_hight = len(Level_map)*tile_size#412
