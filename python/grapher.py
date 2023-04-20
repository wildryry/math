import pygame 

import sys 


clock = pygame.time.Clock() 

screen = pygame.display.set_mode((1000,800))

done = False

pygame.draw.line(screen,(255,255,255),(20,800),(300,50))

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True







    clock.tick(60)




pygame.quit()
sys.exit()            