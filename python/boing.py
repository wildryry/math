
import pygame

import sys 

from random import randint

pygame.init()
pygame.font.init()


screen = pygame.display.set_mode((500,200))
pygame.display.set_caption('your a goober')

back_ground = pygame.Surface((screen.get_width(),screen.get_height()))
back_ground_rect = back_ground.get_rect(topleft = (0,0))
back_ground.fill((255,255,255))

clock = pygame.time.Clock()
number = pygame.font.Font('fonts/data-latin.ttf',50)
since_last_click = 0


pygame.mixer.music.set_volume(0.2)

bage = pygame.image.load('graphics/objects/certified_goober.jpg').convert_alpha()
bage_rect = bage.get_rect(center = (0,100))
bage_speed = 3

funny = 0

clicks = 0

mouse_down = False

while True:
    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mixer.music.get_busy() == False:
                mouse_down = True
                click = pygame.mouse.get_pressed()
                if click[0]:
                    clicks += 1
                    funny +=  1
            else: 
                mouse_down = False


    if funny >= 0.05 and mouse_down == False: 
        funny -= 0.08
        
    

    if bage_rect.right > 450:
        bage_rect.right = 450
        bage_speed = -6.5 - funny 
    
    if bage_rect.left < 50: 
        bage_rect.left = 50
        bage_speed = 6.5 + funny 
    
    if bage_speed < 0:
        bage_speed += .05
    
    if bage_speed > 0:
        bage_speed -= .05
    
    number_display_surface = number.render(f'{clicks}',False,(75,75,75))
    number_display_rect = number_display_surface.get_rect(midbottom = (250,200))
    
    
    screen.blit(back_ground,back_ground_rect)
    screen.blit(bage,bage_rect)
    screen.blit(number_display_surface,number_display_rect)

    
    bage_rect.x += bage_speed    
    
    

    pygame.display.update()
    clock.tick(60)