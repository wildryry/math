

import pygame

import sys

import math as ma

from medevil_tank_setting import *

from medevil_tiles import Tile

from medevil_tank_level import Level

from medevil_tank_player import Player


class Arrow(pygame.sprite.Sprite):    
    def __init__(self, pos , speed, dir):
        super().__init__()
        # what this does is -> cos^-1 (dir.x/1) = Ɵ
        rotation = ma.degrees(ma.acos(dir.x))
        self.orginal_image = pygame.image.load('images/arrow.png')
        self.image = pygame.transform.rotate(self.orginal_image, rotation)
        self.rect = self.image.get_rect(center = pos)

        

        self.dir = dir
        self.speed = speed
        self.vol = speed * dir 
        self.pos = pos
        self.stuck = False
        
        self.rotation = 0#rotation 
        None

    def update(self,delta_time):

        
        

        self.vol = self.vol + gravity * delta_time/1000

        self.pos += self.vol * delta_time/1000

        vector = self.vol.normalize()
        #'''
        if self.stuck == False:
            if self.dir.y < 0 and self.dir.x < 0:
                if vector.y < 0:
                    self.rotation = ma.degrees(ma.acos(vector.x) )+ 180
                    None
                else:
                    self.rotation = ma.degrees(ma.asin(vector.y) ) + 0
                    None

            elif self.dir.y > 0 and self.dir.x > 0:     
                self.rotation = ma.degrees(ma.acos(vector.y) )+ 90
                None

            elif self.dir.y < 0 and self.dir.x > 0:
                if vector.y < 0:
                    self.rotation = ma.degrees(ma.acos(vector.x) )+ 180
                    None
                else:
                    self.rotation = ma.degrees(ma.acos(vector.y) )+ 90
                    None

            elif self.dir.y > 0 and self.dir.x < 0:     
                self.rotation = ma.degrees(ma.asin(vector.y) ) + 0
                None



        

        #print(self.rotation, ma.degrees(self.dir.x))
        

        self.image = pygame.transform.rotate(self.orginal_image, self.rotation)
        

        '''
        for pieces in Level_group:
            if self.rect.colliderect(pieces.rect):
                self.vol = pygame.math.Vector2(0,0)
                self.pos = pygame.math.Vector2(self.rect.x,self.rect.y)
                if self.stuck == False:
                    self.pos += self.vol * delta_time/1000 *5

                    self.rect.x = self.pos.x
                    self.rect.y = self.pos.y

                self.stuck = True
        #'''
        
        
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        
        if self.rect.x > screen_width + 200 or self.rect.y > screen_hight + 200:
            self.kill()
        elif self.rect.x < -200 or self.rect.y < -200:
            self.kill()

        

        

    def draw(self,surface):
        surface.blit(self.image , self.rect)


arrow_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
Level_group =  pygame.sprite.Group()




mouse_x = 0
mouse_y = 0
mouse_down = False
akey = False
skey = False
wkey = False
w_time = 0
dkey = False


clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width,screen_hight)) 
done = False
level = Level(Level_map,screen)



test_tile = pygame.sprite.Group(Tile((400,100),80))







def try_move_player(self, x_vol, y_vol):
    for piece in Level_group:
        self.rect.x += x_vol
        self.rect.y += y_vol

        if self.rect.colliderect(piece):
            self.rect.x -= x_vol
            self.rect.y -= y_vol
            self.vol.y = 0
            None


def sense_key(key):
    keys = pygame.key.get_pressed()
    if keys[key]:
        return True
    else:
        return False
    None



def shoot_arrow(speedorg):
    
    for sprite in player_group:

        player_vector = pygame.math.Vector2(sprite.rect.center)
        arrow_pos = pygame.math.Vector2(sprite.rect.center)

        mouse_vector = pygame.math.Vector2((mouse_x,mouse_y))

        dir = mouse_vector - player_vector
        dir = dir.normalize()

        
        new_vector = pygame.math.Vector2(-15,-30)
        arrow_pos += new_vector


        speed = speedorg * 10
        
        add_arrow(arrow_pos , speed , dir) 
        
   
        


def add_arrow(arrow_pos , speed ,dir):

    

    
    
    
    new_arrow = Arrow(arrow_pos, speed , dir)
    arrow_group.add(new_arrow)
    all_sprites.add(new_arrow)
        
    None
def add_player(amount , x , y):

    for i in range(amount):
        new_player = Player(x, y + ((i-1)*-25))
        player_group.add(new_player)
        all_sprites.add(new_player)
        None







funny = 5

while not done:
    
    

    mouse_x,mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        #if event.type == pygame.MOUSEBUTTONDOWN:
    click = pygame.mouse.get_pressed()
    if click[0] == True:
        mouse_down = True
        shoot_arrow(75)
    else:
        mouse_down = False
            

            

        


        '''
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                wkey = True
                
                None
            
            if event.key == pygame.K_s:
                skey = True
               
                None

            if event.key == pygame.K_SPACE:
                spaceKey = True
                
                
                

            if event.key == pygame.K_a:
                akey = True
                
            

            if event.key == pygame.K_d:
                dkey = True
                
            

        else:
            skey = False
            dkey = False
            akey = False
            wkey = False
            spacekey = False
        #'''


    if sense_key(pygame.K_w):
        for player in player_group:
            if w_time > 20:
                player.vol += pygame.math.Vector2(0,-600)
                
                w_time = 0
            
    w_time += 1
        
    if sense_key(pygame.K_s):
        for player in player_group:
            player.vol += pygame.math.Vector2(0,100)
        None
        
    if sense_key(pygame.K_a):
        for player in player_group:
            player.vol += pygame.math.Vector2(-10,0)
        None

    if sense_key(pygame.K_d):
        for player in player_group:
            player.vol += pygame.math.Vector2(10,0)
        None

    player_group.update(clock.get_time())

    arrow_group.update(clock.get_time())
    

    
   

    screen.fill((3, 77, 61))
    Level_group.draw(screen)
    arrow_group.draw(screen)
    player_group.draw(screen)
    
    level.run()    

    Level_group.update()
    
    

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()

