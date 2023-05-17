import pygame
import sys

pygame.init()

done = False

BLUE = (9, 171, 224)

screen_width = 500
screen_hight = 500
screen = pygame.display.set_mode((screen_width,screen_hight))
screen_surface = pygame.Surface((screen_width,screen_hight))
screen_surface.fill((0,0,0))

rect_surf = pygame.Surface((50,50))
rect = rect_surf.get_rect()
rect_surf.fill(BLUE)
rect.y = 200
rect.x = 100

Vector_rect = pygame.math.Vector2()

clock = pygame.time.Clock() 


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if rect.x - screen_width*0.5 < 0: x_dif = -1*(rect.x - screen_width*0.5)
    else: x_dif = rect.x - screen_width*0.5
    if rect.y - screen_hight*0.5 < 0: y_dif = -1*(rect.y - screen_hight*0.5)
    else: y_dif = rect.y - screen_hight*0.5

    if rect.x < screen_width*0.5:
        rect.x += x_dif*0.1
    elif rect.x > screen_width*0.5:
        rect.x += x_dif*-0.1
    if rect.y < screen_hight*0.5:
        rect.y += y_dif*0.1
    elif rect.y > screen_hight*0.5:
        rect.y += y_dif*-0.1


   

    
    screen.blit(screen_surface, (0,0))
    screen.blit(rect_surf,rect)
    pygame.draw.line(screen, BLUE , (rect.x , rect.y) , (screen_width*0.5 , screen_hight*0.5))
    
    
    
    
    
    pygame.display.flip()
    clock.tick(5)

pygame.quit()
sys.exit()