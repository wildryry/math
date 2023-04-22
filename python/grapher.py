import pygame
import sys
# Set up Pygame
pygame.init()
wn_x = 800
wn_y = 600
size = (wn_x, wn_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Linear Line Graph")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (24, 135, 7)
BLUE = (43, 94, 214)
# Define the equation of the line (y = mx + b)
m = 1
#   100
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

    
    # Color the screen 
    screen.fill(BLACK)


 # Draw the orgin point

    pygame.draw.aaline(screen, BLUE, ((wn_x/2),0), ((wn_x/2),wn_y), 5)
    pygame.draw.aaline(screen, BLUE, (0,(wn_y/2)), (wn_x,(wn_y/2)), 5)


    # Draw the lines
    pygame.draw.aaline(screen, GREEN, ((wn_x/2), -1*b + (wn_y/2)), (wn_x, int(-1*m * wn_x + b + (wn_y/2))), 5)
    
    if m >= 1: pygame.draw.aaline(screen, GREEN, ((wn_x/2), -1*b + (wn_y/2)), (0, int(m * wn_x + b + (wn_y/2))), 5)
    
    else: pygame.draw.aaline(screen, GREEN, ((wn_x/2), -1*b + (wn_y/2)), (0, int(m * wn_x + b + (wn_y/2))), 5) 
    
    
   

    # Update the screen
    pygame.display.flip()
    
    

    # Wait for a short period of time to control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()