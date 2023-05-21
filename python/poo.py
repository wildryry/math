
import pygame 

import sys

from random import randint

pygame.init() 

pygame.display.init()

ground = pygame.image.load('images/ground.png')
sky = pygame.image.load('images/sky.png')




mouse_down = False 




score_text = pygame.font.Font('fonts/data-latin.ttf',40)
time_text = pygame.font.Font('fonts/data-latin.ttf',30)


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
		global score
		global hits
		global misses
		
		self.rect.y += 0.05
		self.time_left += randint(0,1)
		
		

		if self.time_left >= self.time:
			self.kill()

			misses += 1

			None
		
		
		if	self.rect.collidepoint(pygame.mouse.get_pos()) and mouse_down:
			self.kill()

			new_boom = Boom(self.rect.x , self.rect.y , 30)

			boom_group.add(new_boom)

			score += 1

			hits += 1
			
			None
			

			

		
	
	
		
	def draw(self , surface):
		surface.blit(self.image , self.rect)
		

		
class Boom(pygame.sprite.Sprite):
	def __init__(self,x,y,time):
		super().__init__()
		self.image = pygame.image.load('images/caboom.png')
		self.rect = self.image.get_rect(center = (x+44,y+17))
		self.time = time
		
		


	def update(self):
		
		
		if self.time <= 0:
			
			self.kill()
		else:
			self.time += -1

		None

	def draw(self,surface):
		surface.blit(self.image , self.rect)
		None
		

screen_width = 600
screen_hight = 400

score = 0

seconds = 60

time = seconds*60

hits = 0

misses = 0

hit_rate = 0

screen = pygame.display.set_mode((screen_width,screen_hight))

end_backround_surface = pygame.image.load('images/backround.png')
end_backround_rect = end_backround_surface.get_rect(center = (screen_width*.5,screen_hight*0.5))

#boom
boom_group = pygame.sprite.Group()


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
	global score
	

	time = 100


	

	for i in range(amount):
		
		y = randint(70,screen_hight-30)

		x = randint(70,screen_width-50) 
		
		if y <= 410 and y >= 0:
			
			
			new_button = Button(time,x,y)
			button_group.add(new_button)
			all_sprites.add(new_button)



buttons = 5
new_button(buttons)

while not done:

	mouse_group.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			#pygame.quit()
			#sys.exit()	

		if event.type == pygame.KEYDOWN:
			
			print(pygame.key.get_pressed())
	
		if event.type == pygame.MOUSEBUTTONDOWN:

			if len(pygame.sprite.spritecollide(mouse, button_group, False, collided = None)) == 0:
				misses += 1

			mouse_down = True
		else:
			mouse_down = False

		if event.type == pygame.USEREVENT+1:
			None
			if len(button_group) == 0:
				new_button(buttons)

	#time counting down

	time += -1

	seconds = round(time/60)

	if time <= 0:
		done = True
	


	#accuracy logic
		
	if misses != 0:
		
		hit_rate = hits / (hits + misses)

	elif hit_rate > 1:
		hit_rate = 1

	else:
		hit_rate = 1
	
			
		
			
	score_text_surface = score_text.render(f'score:{round(score*hit_rate)} hit rate:{round(hit_rate*100)}%',False,(75,75,75))
	score_text_rect = score_text_surface.get_rect(center = (screen_width / 2, screen_hight*0.05))
			
	time_text_surface = time_text.render(f'time:{seconds}', False, (75,75,75))
	time_text_rect = time_text_surface.get_rect(topleft = (screen_width*0.01,screen_hight*0.13))

	

	screen.blit(sky,(0,0))
	screen.blit(ground ,(0,360))
	screen.blit(score_text_surface , score_text_rect)
	screen.blit(time_text_surface,time_text_rect)

	button_group.update()

	boom_group.update()
	
	

	#mouse sprite things
	
	
	


	



	button_group.draw(screen)

	boom_group.draw(screen)

	mouse_group.draw(screen)
	
	
	
	pygame.display.update()
	clock.tick(60)


done = False

score_text = pygame.font.Font('fonts/data-latin.ttf',21)

final_score_text = pygame.font.Font('fonts/data-latin.ttf',23)

tortus_surface = pygame.image.load('images/boogie_tortus_transparent.png')
tortus_rect = tortus_surface.get_rect(center = (screen_width * 0.45 , screen_hight * 0.47))



while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True


	mouse_group.update()

	final_score_text_surface = final_score_text.render(f'your final score is :{round(score*hit_rate)}',False , (75,75,75))
	final_score_text_rect = final_score_text_surface.get_rect(center = (screen_width*0.46 , screen_hight*0.56))

	score_text_surface = score_text.render(f'total hits:{hits}  rate:{round(hit_rate*100)}%',False,(75,75,75))
	score_text_rect = score_text_surface.get_rect(center = (screen_width * 0.46, screen_hight * 0.38))



	screen.blit(end_backround_surface,end_backround_rect)

	screen.blit(score_text_surface,score_text_rect)

	screen.blit(final_score_text_surface , final_score_text_rect)

	screen.blit(tortus_surface,tortus_rect)
	
	mouse_group.draw(screen)
	
	pygame.display.update()
	clock.tick(60)



pygame.quit()
sys.exit()	