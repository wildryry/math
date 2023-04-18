import pygame 

import sys

from random import randint

pygame.init() 

pygame.display.init()

ground = pygame.image.load('images/ground.png')
sky = pygame.image.load('images/sky.png')



class Mouse(pygame.sprite.Sprite):
	def __init__(self,pos_x,pos_y):
		super().__init__()
		self.image = pygame.image.load('images/man from the poster transparent.png').convert_alpha()
		self.rect = self.image.get_rect()
		pos_x = self.rect.x
		pos_y = self.rect.y
	
	def update(self):
		self.rect.center = pygame.mouse.get_pos()

class Button(pygame.sprite.Sprite):
	def __init__(self, time, pos_x, pos_y,):
		super().__init__()
		self.image = pygame.image.load('images/boogie_button.png')
		self.rect = self.image.get_rect()
		self.time = time
	
	def update(self):
		gf = 2
		

		


screen = pygame.display.set_mode((ground.get_width(),400))


#Button
button = Button(10000,0,0)
button_group = pygame.sprite.Group()


#mouse
mouse = Mouse(300,200)
mouse_group = pygame.sprite.Group()
mouse_group.add(mouse)


back_ground_rect = pygame.Surface.get_rect(screen)

done = False

pygame.mouse.set_visible(False) 


clock = pygame.time.Clock()  

pygame.time.set_timer(pygame.USEREVENT+1, 1100)


for x in range(100):

	button.rect.y = randint(10,390)
	button.rect.x = randint(0,600)
	button_group.add(button)

while not done:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.KEYDOWN:
			
			print(pygame.key.get_pressed())
	
		if event.type == pygame.USEREVENT+1:
			print('event')
			button_group.add(button)

	

	screen.blit(sky,(0,0))
	screen.blit(ground ,(0,360))
	
	button_group.update()
	button_group.draw(screen)
	
	
	#mouse sprite things
	
	mouse_group.update()
	mouse_group.draw(screen)

	pygame.display.update()
	clock.tick(60)


pygame.quit()
sys.exit()	