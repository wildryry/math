
import pygame 
from medieval_tiles import Tile
from medieval_tank_setting import *
from medieval_tank_player import Player
from medieval_enemey_1 import Enemey 
from medieval_arrow import Arrow


class Level:

    def __init__(self, level_data, surface):
        self.display_surface = surface 
        self.world_shift = 0
        self.mouse_down = False
        self.mouse_delay = -1 # <-  in seconds
        self.mouse_time = self.mouse_delay*60
        self.setup_level(level_data)
        self.find_rim()
                
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.arrows = pygame.sprite.Group()
        self.enemeys = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):

                #this places all the tiles based off of the level_data

                x = tile_size*col_index
                y = tile_size*row_index
                
                if cell == 'X':

                    tile = Tile((x,y), tile_size, 'rock', self.display_surface)
                    self.tiles.add(tile)
              
                if cell == 'P':

                    player_sprite = Player(screen_width/2,y)
                    self.world_shift = -x + screen_width/2
                    self.player.add(player_sprite)
                    
                if cell == 'B':

                    tile = Tile((x,y), tile_size, 'blue', self.display_surface)
                    self.tiles.add(tile)

                if cell == 'G':

                    tile = Tile((x,y), tile_size, 'ladder', self.display_surface)
                    self.tiles.add(tile)

                if cell == 'E':
                    enemey_sprite = Enemey((x,y))
                    self.enemeys.add(enemey_sprite)

    def find_rim(self):
        for sprite in self.tiles.sprites():
            for tile in self.tiles.sprites():
                #if tile.rect.collidepoint(sprite.pos[0]+40,sprite.pos[1]-40) != True and tile.color != 'blue': 
                    #sprite.switch_texture(2)
                    #None
                #if tile.rect.collidepoint(sprite.pos[0]+120,sprite.pos[1]+40) != True and tile.color != 'blue' and tile.rect.collidepoint(sprite.pos[0]+40,sprite.pos[1]-40) != True   : 
                    #print('1')
                    #sprite.switch_texture(3)
                None   
                    
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
            if sprite.rect.colliderect(player.rect) and sprite.collision == True:
                if player.vol.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.vol.x > 0:
                    player.rect.right = sprite.rect.left

    def vert_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect) and sprite.collision == True or sprite.rect.colliderect(player.rect) and sprite.color == 'green':
                if player.vol.y < 0  and sprite.collision == True:
                    player.rect.top = sprite.rect.bottom
                    
                elif player.vol.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.grounded = True
                    player.vol.y * -1
                player.vol.y = 0
                
    def arrow_collision(self):
        
        for arrow in self.arrows:
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(arrow.hit_box) and sprite.collision == True:
                    arrow.stick()
            
    def shoot_arrow(self, speedorg, time):
        
        mouse_x,mouse_y = pygame.mouse.get_pos()

        for sprite in self.player:

            player_vector = pygame.math.Vector2(sprite.rect.center)
            arrow_pos = pygame.math.Vector2(sprite.rect.center)

            mouse_vector = pygame.math.Vector2((mouse_x,mouse_y))

            dir = mouse_vector - player_vector
            dir = dir.normalize()

            
            new_vector = pygame.math.Vector2(-15,-30)
            arrow_pos += new_vector


            speed = speedorg * 10
            
            new_arrow = Arrow(arrow_pos, speed , dir, time)
            self.arrows.add(new_arrow)
    
    def run(self,clock):

        #enemey
        self.enemeys.draw(self.display_surface)
        self.enemeys.update(self.world_shift, self.display_surface, self.arrows)

        #tiles       
        self.tiles.draw(self.display_surface)
        self.tiles.update(self.world_shift)
        

        #arrows
        self.arrows.update(clock.get_time(),self,self.display_surface)
        self.arrow_collision()
        self.arrows.draw(self.display_surface)
        
        
        #mouse input
        click = pygame.mouse.get_pressed()
        if click[0] == True and self.mouse_time >= self.mouse_delay*60:
            self.shoot_arrow(75, 5)
            self.mouse_down = True
            self.mouse_time = 0
        else:
            self.mouse_time += 1
            self.mouse_down = False
        
        #tile scoll
        self.scroll_x()    

        #player
        self.player.update()
        self.horiz_movement_collision()
        self.vert_movement_collision()
        self.player.draw(self.display_surface)
        player = self.player.sprite
        player.head.draw(self.display_surface)
        
        
        
        
        
       
