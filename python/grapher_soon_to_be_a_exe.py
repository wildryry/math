import pygame
import sys
# Set up Pygame
pygame.init()
wn_x = 800
wn_y = 800
size = (wn_x, wn_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Linear Line Graph")

# Fonts
text = pygame.font.Font('fonts/data-latin.ttf',50)


# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (24, 135, 7)
BLUE = (43, 94, 214)
# Define the equation of the line (y = mx + b)

rise = 0

run = 3
#m = (rise/run)/2
b = 0



rise_choosen = False

unfinshed = True

clock = pygame.time.Clock()

while unfinshed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:

            if rise_choosen == False:    
                if event.key == pygame.K_UP:
                    rise += 1
            else:
                if event.key == pygame.K_UP:
                    run += 1       
            
            if event.key == pygame.K_DOWN:
                if rise_choosen == False:    
                    if rise >= 1:
                        rise += -1    
                else:
                    if run >= 2:
                        run += -1
            if event.key == pygame.K_RETURN:
                if rise_choosen == False:
                    rise_choosen = True
                else:
                    unfinshed = False
    

    screen.fill(WHITE)

    if rise_choosen == False:    
        
        rise_number_surface = text.render(f'Rise :{rise}',False,GREEN)
        rise_number_rect = rise_number_surface.get_rect(midtop = ((wn_x/2),(wn_y/2 + 100)))

        screen.blit(rise_number_surface,rise_number_rect)
    else:
        
        run_number_surface = text.render(f'Run :{run}',False,GREEN)
        run_number_rect = run_number_surface.get_rect(midtop = ((wn_x/2),(wn_y/2 + 200)))

        screen.blit(run_number_surface,run_number_rect)
        screen.blit(rise_number_surface,rise_number_rect)


    pygame.display.flip()

m = (rise/run)/2
# Define the x and y values to plot
x_values = range(0, 800)
y_values = [int(m * x + b) for x in x_values]


# Loop until the user clicks the close button
done = False


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