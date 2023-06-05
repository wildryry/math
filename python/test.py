

import pygame

import sys

import math as ma


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('images/tank_sprite.png')
        self.rect = self.image.get_rect(center = (x,y))
        self.rect.x = x
        self.rect.y = y

    def update(self):

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
        self.pos = pos
        
        self.rotation = rotation
        None

    def update(self):

        
        print(self.dir.y)
        if self.dir.y < 0 or self.dir.y == 0:
            if self.dir.y != 0 and self.dir.y % 360 != 0:
                self.rotation = (ma.degrees(ma.acos(self.dir.y)) + 180)
                self.speed -= gravity
                self.dir -= gravity
            
        else:
            if self.dir.y != 0 and self.dir.y % 360 != 0:
                self.rotation = ma.degrees(ma.acos(-self.dir.y))
                self.speed += gravity
                self.dir += gravity 

        #print(self.rotation, ma.degrees(self.dir.x))
        

        self.image = pygame.transform.rotate(self.orginal_image, self.rotation)
        print(self.speed.y)
        
        self.speed += pygame.math.Vector2(0,0)        
        
        
        self.rect.x += (self.dir.x * self.speed.x)
        self.rect.y += (self.dir.y * (self.speed.y + 5))
        
        if self.rect.x > screen_width or self.rect.y > screen_hight:
            self.kill()
        elif self.rect.x < -75 or self.rect.y < -75:
            self.kill()

        

        

    def draw(self,surface):
        surface.blit(self.surface , self.rect)


arrow_group = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

player_group = pygame.sprite.Group()

screen_width = 1000
screen_hight = 412

gravity = pygame.math.Vector2(0,0.5)

mouse_x = 0

mouse_y = 0

mouse_down = False

akey = False

dkey = False

clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width,screen_hight)) 

done = False

def diff(num1, num2):
    if num1 == num2:
        return 1
        None
    elif num1 > num2:
        return num1 - num2
        None
    else:
        return num2 - num1
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


        speed = pygame.math.Vector2(speedorg)
        
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
#add_player(1, 500, 250)



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
                shoot_arrow(10)
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
                for sprite in player_group:
                    sprite.rect.x += -sprite.image.get_width()
                    None
            

            if event.key == pygame.K_d:
                dkey = True
                for sprite in player_group:
                    sprite.rect.x += sprite.image.get_width()
                None
            

        else:
            skey = False
            dkey = False
            akey = False
            wkey = False
            spacekey = False

    
    

    screen.fill((3, 77, 61))
    arrow_group.draw(screen)
    player_group.draw(screen)
    

    arrow_group.update()

    

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()

