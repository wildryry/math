import pygame

import math as ma

class Head1(pygame.sprite.Sprite):
    def __init__(self, tank_pos):
        super().__init__()
        self.image = pygame.image.load('images/tank_head1.png')
        self.image = pygame.transform.scale_by(self.image, 5)
        self.origonal_image = self.image
        self.rect = self.image.get_rect(center = tank_pos)
        self.rect.y += -30

        self.rotation = 0

    def update(self, tank_pos, filpped):
        

        #finding the rotation to point at the mouse
        mouse_x , mouse_y = pygame.mouse.get_pos()
        head_pos = self.rect.center

        #distance to the mouse
        x_dis = mouse_x - head_pos[0]   
        y_dis = mouse_y - head_pos[1]
        
        #rotating the head
        if x_dis == 0: x_dis = 1
        if x_dis < 0: self.rotation = ma.degrees(ma.atan(-y_dis/x_dis)) +90
        if x_dis > 0: self.rotation = ma.degrees(ma.atan(-y_dis/x_dis)) +270
        self.image = pygame.transform.rotate(self.origonal_image, self.rotation)

        #keeps head on the player plus an offset
        self.rect.center = tank_pos
        self.rect.y += -30

        pass

    def draw(self, display):
        display.blit(self.image, self.rect)
        print(self.rect)
        pass