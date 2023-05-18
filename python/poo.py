from tkinter import CENTER
import pygame 

import sys

from random import randint

pygame.init() 

pygame.display.init()

ground = pygame.image.load('images/ground.png')
sky = pygame.image.load('images/sky.png')


mouse_down = False 
score = 0

score_text = pygame.font.Font('fonts/data-latin.ttf',50)


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
		self.rect = self.image.get_rect(center = (pos_x,pos_y))
		#self.rect.x = pos_x
		#self.rect.y = pos_y
		self.time = randint(time,time+50)
		self.time_left = 0
		if pygame.sprite.spritecollide(self, button_group, True, collided = None):
			self.kill()
			new_button(1)

	
	def update(self):
		
		self.rect.y += 0.05
		self.time_left += randint(0,1)
		
		

		if self.time_left >= self.time:
			self.kill()
			None
		
			
		if	self.rect.collidepoint(pygame.mouse.get_pos()) and mouse_down:
			self.kill()
			
			None
			

		
	
	
		
	def draw(self , surface):
		surface.blit(self.image , self.rect)
		

		

		

screen_width = 600
screen_hight = 400


screen = pygame.display.set_mode((screen_width,screen_hight))


#Button

button_group = pygame.sprite.Group()



#mouse
mouse = Mouse(300,200)
mouse_group = pygame.sprite.Group()
mouse_group.add(mouse)


#all sprites
all_sprites = pygame.sprite.Group()

all_sprites.add(mouse)



back_ground_rect = pygame.Surface.get_rect(screen)

done = False

pygame.mouse.set_visible(False) 


clock = pygame.time.Clock()  

pygame.time.set_timer(pygame.USEREVENT+1, 1)

funny = 0

def new_button(amount):
	
	

	for i in range(amount):
		
		y = randint(30,screen_hight-30)

		x = randint(50,screen_width-50) 
		
		if y <= 410 and y >= 0:
			
			
			new_button = Button(75,x,y)
			button_group.add(new_button)
			all_sprites.add(new_button)



buttons = 5
new_button(buttons)

while not done:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.KEYDOWN:
			
			print(pygame.key.get_pressed())
	
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_down = True
		else:
			mouse_down = False

		if event.type == pygame.USEREVENT+1:
			None
			if len(button_group) == 0:
				new_button(buttons)
			
			
		
			
	score_text_surface = score_text.render(f'{score}',False,(75,75,75))
	score_text_rect = score_text_surface.get_rect(center = (screen_width / 2, screen_hight*0.1))
			


	

	screen.blit(sky,(0,0))
	screen.blit(ground ,(0,360))

	button_group.update()
	
	

	#mouse sprite things
	
	
	


	mouse_group.update()

	button_group.draw(screen)
	mouse_group.draw(screen)
	
	
	
	pygame.display.update()
	clock.tick(60)


pygame.quit()
sys.exit()	