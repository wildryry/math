import pygame

from setting import *

from wall import Wall

class Level:

    def __init__(self, display_surface):
        global level_layout
        self.level_data = level_layout
        self.display = display_surface
        self.set_up(self.level_data)

    def set_up(self, level_data):
        global tile_size
        self.tiles = pygame.sprite.Group()

        for row_index,row in enumerate(self.level_data):
            for col_index,cell in enumerate(row):

                x = tile_size*col_index
                y = tile_size*row_index
                
                if cell == 'W':

                    tile = Wall((x,y), tile_size, self.display)
                    self.tiles.add(tile)
                    print(x,y)
    def run(self):
        self.tiles.draw(self.display)
        