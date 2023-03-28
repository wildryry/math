import pygame 

import sys

from random import randint

pygame.init() 

pygame.display.init()

ground = pygame.image.load('ground.png')
sky = pygame.image.load('sky.png')

button_list = []

class Mouse(pygame.sprite.Sprite):
	def __init__(self,pos_x,pos_y):
		super().__init__()
		self.image = pygame.image.load('mouse.png').convert_alpha()
		self.rect = self.image.get_rect()

def button_draw():
	global button_list
	
	for x in button_list:
		
		
		screen.blit(button_surface,x.x(randint(0,300)))
		


screen = pygame.display.set_mode((ground.get_width(),400))
guy = pygame.image.load('mouse.png').convert_alpha()
guy_rect = guy.get_rect(topleft = pygame.mouse.get_pos())

mouse = Mouse(300,200)

mouse_group = pygame.sprite.Group()
mouse_group.add(mouse)


button_surface = pygame.image.load('boogie_button.png').convert_alpha()
button_rect = button_surface.get_rect(center = (300,200))

back_ground_rect = pygame.Surface.get_rect(screen)

done_not = True

pygame.mouse.set_visible(False) 


clock = pygame.time.Clock()  

pygame.time.set_timer(pygame.USEREVENT+1, 1100)

while done_not:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done_not = False

		if event.type == pygame.KEYDOWN:
			
			print(pygame.key.get_pressed())
	
		if event.type == pygame.USEREVENT+1:
			button_list.append(button_rect)
			

	

	screen.blit(sky,(0,0))
	screen.blit(ground ,(0,360))
	
	
	
	#button_draw()
	#mouse sprite things
	mouse.pos_x = pygame.mouse.get_pos()
	mouse_group.draw(screen)

	pygame.display.update()
	clock.tick(60)


pygame.quit()
sys.exit()	