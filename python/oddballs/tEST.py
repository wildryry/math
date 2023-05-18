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
mid = (screen_width*0.5,screen_hight*0.5)


rect_surf = pygame.Surface((50,50))
rect = rect_surf.get_rect()
rect_surf.fill(BLUE)
rect.y = 100
rect.x = -1000
rect_speed = 0.1

Vector_rect = pygame.math.Vector2()

clock = pygame.time.Clock() 

def move_point(rect,end_point):
    
    rect_speed = 0
    
    if rect.x - end_point[0] < 0: x_dif = -1*(rect.x - end_point[0])
    else: x_dif = rect.x - end_point[0]
    if rect.y - end_point[1] < 0: y_dif = -1*(rect.y - end_point[1])
    else: y_dif = rect.y - end_point[1]

    if x_dif == 0 and y_dif == 0:
        rect_speed = 0
        rect.x = end_point[0]
        rect.y = end_point[1]
    elif rect_speed < 1:
        rect_speed += 0.15 

    if rect.x < end_point[0]:
        rect.x += x_dif*rect_speed
    elif rect.x > end_point[0]:
        rect.x += x_dif*-rect_speed
    if rect.y < end_point[1]:
        rect.y += y_dif*rect_speed
    elif rect.y > end_point[1]:
        rect.y += y_dif*-rect_speed

    return rect

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    
    #if rect.x - screen_width*0.5 < 0: x_dif = -1*(rect.x - screen_width*0.5)
    #else: x_dif = rect.x - screen_width*0.5
    #if rect.y - screen_hight*0.5 < 0: y_dif = -1*(rect.y - screen_hight*0.5)
    #else: y_dif = rect.y - screen_hight*0.5

    #if x_dif == 0 and y_dif == 0:
    #    rect_speed = 0
    #else: rect_speed += 0.05

    #if rect.x < screen_width*0.5:
    #    rect.x += x_dif*rect_speed
    #elif rect.x > screen_width*0.5:
    #    rect.x += x_dif*-rect_speed
    #if rect.y < screen_hight*0.5:
    #    rect.y += y_dif*rect_speed
    #elif rect.y > screen_hight*0.5:
    #    rect.y += y_dif*-rect_speed

    rect = move_point(rect,mid)
   

    
    screen.blit(screen_surface, (0,0))
    screen.blit(rect_surf,rect)
    pygame.draw.line(screen, BLUE , (rect.x , rect.y) , (screen_width*0.5 , screen_hight*0.5))
    
    
    
    
    
    pygame.display.flip()
    clock.tick(5)

pygame.quit()
sys.exit()