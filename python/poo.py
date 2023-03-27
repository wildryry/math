import pygame 

import sys

pygame.init() 

pygame.display.init()

ground = pygame.image.load('ground.png')
sky = pygame.image.load('sky.png')


screen = pygame.display.set_mode((ground.get_width(),400))
guy = pygame.image.load('mouse.png').convert_alpha()
guy_rect = guy.get_rect(topleft = pygame.mouse.get_pos())

back_ground_rect = pygame.Surface.get_rect(screen)

done_not = True

pygame.mouse.set_visible(False) 

while done_not:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done_not = False

		if event.type == pygame.KEYDOWN:
			
			print(pygame.key.get_pressed())
	
	guy_rect = guy.get_rect(center = pygame.mouse.get_pos())

	screen.blit(sky,(0,0))
	screen.blit(ground ,(0,360))
	screen.blit(guy ,guy_rect)
	


	pygame.display.update()

pygame.quit()
sys.exit()	