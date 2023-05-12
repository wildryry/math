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
		self.image = pygame.image.load('images/mouse.png').convert_alpha()
		self.rect = self.image.get_rect()
		pos_x = self.rect.x
		pos_y = self.rect.y
	
	def update(self):
		self.rect.topleft = pygame.mouse.get_pos()

class Button(pygame.sprite.Sprite):
	def __init__(self, time, pos_x, pos_y,):
		super().__init__()
		self.image = pygame.image.load('images/boogie_button.png')
		self.rect = self.image.get_rect()
		self.time = time
	
	def update(self):
		
		self.image = pygame.image.load('images/boogie_button.png')
		self.rect = self.image.get_rect()
		self.rect.x += 0.01
		self.rect.y += 0.5

		
		
		

		


screen = pygame.display.set_mode((ground.get_width(),400))


#Button
button = Button(100,300,200)
button_group = pygame.sprite.Group()


#mouse
mouse = Mouse(300,200)
mouse_group = pygame.sprite.Group()
mouse_group.add(mouse)


#all sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(mouse)
all_sprites.add(button)

back_ground_rect = pygame.Surface.get_rect(screen)

done = False

pygame.mouse.set_visible(False) 


clock = pygame.time.Clock()  

pygame.time.set_timer(pygame.USEREVENT+1, 1100)



def buuton():
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
			print('event' , all_sprites)
			

	

	screen.blit(sky,(0,0))
	screen.blit(ground ,(0,360))
	

	button_group.update()
	

	#mouse sprite things
	
	mouse_group.update()


	for enitys in all_sprites:
		screen.blit(enitys.image, enitys.rect)
	
	
	pygame.display.update()
	clock.tick(60)


pygame.quit()
sys.exit()	