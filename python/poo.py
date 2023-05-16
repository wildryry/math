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
		self.rect.x = pos_x
		self.rect.y = pos_y
	
	def update(self):
		self.rect.topleft = pygame.mouse.get_pos()

	def draw(self , surface):
		surface.blit(self.image , self.rect)

class Button(pygame.sprite.Sprite):
	def __init__(self, time, pos_x, pos_y,):
		super().__init__()
		self.image = pygame.image.load('images/boogie_button.png')
		self.rect = self.image.get_rect()
		self.time = time
		self.rect.x = pos_x
		self.rect.y = pos_y
	
	def update(self):
		
		self.rect.y += 1
		print(self.rect.y)

		if self.rect.y <= 410:
			self.kill()
		
	def draw(self , surface):
		surface.blit(self.image , self.rect)
		

		
def heheha(low , high):
	return randint(low,high)
		

		


screen = pygame.display.set_mode((ground.get_width(),400))


#Button
new_button = Button(100,200,200)
button_group = pygame.sprite.Group()
button_group.add(new_button)


#mouse
mouse = Mouse(300,200)
mouse_group = pygame.sprite.Group()
mouse_group.add(mouse)


#all sprites
all_sprites = pygame.sprite.Group()

all_sprites.add(mouse)
all_sprites.add(new_button)


back_ground_rect = pygame.Surface.get_rect(screen)

done = False

pygame.mouse.set_visible(False) 


clock = pygame.time.Clock()  

pygame.time.set_timer(pygame.USEREVENT+1, 1100)

funny = 0

def buuton(offset,x,y):
	
	

	for i in range(15):
		
		newy = i * offset + y
		
		if y <= 410:
			
			
			new_button = Button(100,x,newy)
			button_group.add(new_button)
			all_sprites.add(new_button)





while not done:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.KEYDOWN:
			
			print(pygame.key.get_pressed())
	
		if event.type == pygame.USEREVENT+1:
			print('event' , all_sprites)
			button_group.add(new_button)
			all_sprites.add(new_button)
			

	

	screen.blit(sky,(0,0))
	screen.blit(ground ,(0,360))

	button_group.update()
	
	

	#mouse sprite things
	

	mouse_group.update()

	all_sprites.draw(screen)
	
	
	
	pygame.display.update()
	clock.tick(60)


pygame.quit()
sys.exit()	