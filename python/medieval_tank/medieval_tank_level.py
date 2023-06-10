import pygame 
from medieval_tiles import Tile
from medieval_tank_setting import *
from medieval_tank_player import Player



class Level:

    def __init__(self, level_data, surface):
        self.display_surface = surface 
        self.setup_level(level_data)
        
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.arrows = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):

                x = tile_size*col_index
                y = tile_size*row_index
                
                if cell == 'X':

                    tile = Tile((x,y), tile_size, 'orange')
                    self.tiles.add(tile)
                
                if cell == 'P':

                    player_sprite = Player(x,y)
                    self.player.add(player_sprite)
                    
                if cell == 'B':

                    tile = Tile((x,y), tile_size, 'blue')
                    self.tiles.add(tile)

                if cell == 'G':

                    tile = Tile((x,y), tile_size, 'green')
                    self.tiles.add(tile)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        dir_x = player.vol.x

        if player_x < screen_width*0.25 and dir_x < 0:
            self.world_shift = 5
            player.speed = 0
            

        elif player_x > screen_width - (screen_width*0.25) and dir_x > 0:
            self.world_shift = -5
            player.speed = 0
            
        else:
            self.world_shift = 0
            player.speed = 8

    def horiz_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.vol.x * player.speed 

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect) and sprite.color == 'orange':
                if player.vol.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.vol.x > 0:
                    player.rect.right = sprite.rect.left

    def vert_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect) and sprite.color == 'orange' or sprite.rect.colliderect(player.rect) and sprite.color == 'green':
                if player.vol.y < 0  and sprite.color == 'orange':
                    player.rect.top = sprite.rect.bottom
                elif player.vol.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.grounded = True
                player.vol.y = 0

    def arrow_collision(self):
        
        for arrow in self.arrows:
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(arrow.rect) and sprite.color == 'orange':
                    arrow.kill()
            pass

    def run(self,clock):
        #tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        #arrows
        self.arrows.update(clock.get_time(),self)
        self.arrow_collision()
        self.arrows.draw(self.display_surface)

        #player
        self.player.update()
        self.horiz_movement_collision()
        self.vert_movement_collision()
        self.player.draw(self.display_surface)
        
        
        
       
