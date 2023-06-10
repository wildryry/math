import pygame 
from medevil_tiles import Tile
from medevil_tank_setting import *
from medevil_tank_player import Player

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface 
        self.setup_level(level_data)
        
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                if cell == 'X':

                    x = tile_size*col_index
                    y = tile_size*row_index

                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'P':

                    x = tile_size*col_index
                    y = tile_size*row_index

                    player = Player(x,y)
                    self.player.add(player)
                    

    def run(self):
        self.tiles.update(0)
        self.tiles.draw(self.display_surface)
        pass
