import pygame

pygame.display.set_caption('medieval_tank')

Level_map =[
    
    
    '                                                                                                                        ',
    '                                                                                                                        ',
    '                                                                                                                        ',
    '       E                 XXXXX              E                                                                           ',
    '      XX                 B   B            XXXXX                                                                         ',
    '     XX                  X   X            B P B                                          XXXX                           ',
    '    XX                   B E B            XXGXX                                         B    B                          ',
    '    XX             X    XXGGGXX    X    XXBBGBBXX       G                               X    X                          ',
    '   XXX             X    B     B    B  XXBBBBBBBBBXX     G                               XE   X              E           ',
    '  XXXXX       XX   X    B     B    B    B   B   B            E                          XXBBXX             XX           ',
    ' XXXXXXX  E   BB   X    XXXXXXX   XXXXXXXXXXXXXXXXXX       XXXXXX  E                    BB  BB       E    XBBX          ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']


tile_size = 80

#for arrows
gravity = pygame.math.Vector2(0,700)

screen_width = 1500#len(Level_map[0])*tile_size
screen_hight = len(Level_map)*tile_size#412
