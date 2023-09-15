import pygame
import math as ma
from medieval_tank_setting import *


class Arrow(pygame.sprite.Sprite):    
    def __init__(self, pos , speed, dir, time):
        super().__init__()
        # what this does is -> cos^-1 (dir.x/1) = Ɵ
        rotation = ma.degrees(ma.acos(dir.x))
        self.orginal_image = pygame.image.load('images/arrow.png')
        self.image = pygame.transform.rotate(self.orginal_image, rotation)
        self.rect = self.image.get_rect(center = pos)
        self.hit_box = pygame.Rect(pos , (15,15))
        self.hit_box.center = pos
        #self.airslow = 25.5
        
        self.gravity = gravity

        self.dir = dir
        self.speed = speed
        self.vol = speed * dir 
        self.pos = pos
        self.stuck = False
        self.death_time = time*60
        
        self.rotation = 0#rotation 
        None

    def update(self,delta_time,level,surface):
        self.hit_box.center = self.rect.center
        '''
        if self.vol.x < 0:
                    self.vol.x += self.airslow
        elif self.vol.x > 0: 
                    self.vol.x -= self.airslow
        '''
        self.vol = self.vol + self.gravity * delta_time/1000

        self.pos += self.vol * delta_time/1000
        self.pos.x += level.world_shift
        vector = self.vol.normalize()

        #rotation

        if self.stuck == False:
            if self.dir.y <= 0 and self.dir.x <= 0:
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
             
                

            vector2 = vector*15

            self.hit_box.x = vector2.x + self.pos.x + 15
            self.hit_box.y = vector2.y + self.pos.y + 15
        
        

        #print(self.rotation, ma.degrees(self.dir.x))
        
        #pygame.draw.rect(surface, 'red', self.hit_box, width = 50)
        self.image = pygame.transform.rotate(self.orginal_image, self.rotation)
        
        if self.stuck:

            if self.death_time <= 0:
                self.kill()
            else:
                self.death_time += -1
            self.vol = pygame.math.Vector2(0,0)
            self.vol *= 0
            self.rect.x = self.pos.x 
        else:
        
            

            self.rect.x = self.pos.x 
            self.rect.y = self.pos.y
            
            if self.rect.x > screen_width + 500 or self.rect.y > screen_hight + 500:
                self.kill()
            elif self.rect.x < -500 or self.rect.y < -1000:
                self.kill()       

    def stick(self):
        self.stuck = True

        pass

    def draw(self,surface):
        surface.blit(self.image , self.rect)
        
        