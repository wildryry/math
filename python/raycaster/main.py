import pygame 
from level import Level
from setting import *

pygame.init

running = True

clock = pygame.time.Clock()

display = pygame.display.set_mode((screen_width, screen_hight))

level = Level(display)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    level.run()

    clock.tick(60)
