import pygame
import sys
# Set up Pygame
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Linear Line Graph")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (24, 135, 7)
BLUE = (43, 94, 214)
# Define the equation of the line (y = mx + b)
m = 2
b = 0

# Define the x and y values to plot
x_values = range(0, 800)
y_values = [int(m * x + b) for x in x_values]

# Loop until the user clicks the close button
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    
    

    # Clear the screen test.py
    screen.fill(BLACK)

    # Draw the line
    pygame.draw.aaline(screen, GREEN, [400, (-1*b + 300)], [800, int(-1*m * 800 + b)], 5)
    pygame.draw.aaline(screen, GREEN, [400, (-1*b + 300)], [800, int(*m * 800 + b)], 5)
    
    # Update the screen
    pygame.display.flip()
    
    

    # Wait for a short period of time to control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()