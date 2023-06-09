

import pygame

import sys

import math as ma

class Level_piece(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('images/platform.png')
        self.rect = self.image.get_rect(center = (x,y))
        self.rect.x = x
        self.rect.y = y

    def update(self):

       

        None

    def draw(self, surface):
        surface.blit(self.image , self.rect)
        
        None


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('images/tank_sprite.png')
        self.rect = self.image.get_rect(center = (x,y))

        self.pos = pygame.math.Vector2(x,y)

        self.vol = pygame.math.Vector2(0,0)

        self.rect.x = x
        self.rect.y = y

    def update(self,delta_time):

        
        self.vol = self.vol + gravity * delta_time/1000

        self.pos += self.vol * delta_time/1000
        for sprite in Level_group:
            if self.rect.colliderect(sprite.rect):
                
                
                self.pos += pygame.math.Vector2(0,-1)
                self.vol = pygame.math.Vector2(0,0)
                
                None

        
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        None

    def draw(self, surface):
        surface.blit(self.image , self.rect)
        None


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



        #'''

        #print(self.rotation, ma.degrees(self.dir.x))
        

        self.image = pygame.transform.rotate(self.orginal_image, self.rotation)
        

        for pieces in Level_group:
            if self.rect.colliderect(pieces.rect):
                self.vol = pygame.math.Vector2(0,0)
                self.pos = pygame.math.Vector2(self.rect.x,self.rect.y)
                if self.stuck == False:
                    self.pos += self.vol * delta_time/1000 *5

                    self.rect.x = self.pos.x
                    self.rect.y = self.pos.y

                self.stuck = True
        
        
        
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

screen_width = 1000
screen_hight = 412


gravity = pygame.math.Vector2(0,700)

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

def move_player():
    None


def sense_key(key):
    keys = pygame.key.get_pressed()
    if keys[key]:
        return True
    else:
        return False
    None


def add_level_piece(x_pos,y_pos):
    
    new_Level_piece = Level_piece(x_pos - 400, y_pos)
    Level_group.add(new_Level_piece)
    all_sprites.add(new_Level_piece)    

    None

def shoot_arrow(speedorg):
    
    for sprite in player_group:

        player_vector = pygame.math.Vector2(sprite.rect.center)
        arrow_pos = pygame.math.Vector2(sprite.rect.center)

        mouse_vector = pygame.math.Vector2((mouse_x,mouse_y))

        dir = mouse_vector - player_vector
        dir = dir.normalize()

        
        new_vector = pygame.math.Vector2(10,-20)
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


add_player(1, 500, 100)

add_level_piece(screen_width*0.5,screen_hight*0.75)


funny = 5

while not done:
    
    

    mouse_x,mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pressed()
            if click[0] == True:
                mouse_down = True
                shoot_arrow(75)
            else:
                mouse_down = False


            

        else: mouse_down = False



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

    if sense_key(pygame.K_w):
        for player in player_group:
            if w_time > 20:
                player.vol += pygame.math.Vector2(0,-600)
                print('up' , w_time)
                w_time = 0
            else:
                w_time += 1
        None
    if sense_key(pygame.K_s):
        for player in player_group:
            player.vol += pygame.math.Vector2(0,100)
        None
        

    player_group.update(clock.get_time())

    arrow_group.update(clock.get_time())
    

    
   

    screen.fill((3, 77, 61))
    Level_group.draw(screen)
    arrow_group.draw(screen)
    player_group.draw(screen)
    

    Level_group.update()
    
    

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()

