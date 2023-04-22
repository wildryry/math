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

# Define a new surface and rect

image_surface = pygame.image.load('images/man from the poster transparent.png')
image_rect = image_surface.get_rect(midtop = ((wn_x/2),(wn_y/2 - 300)))

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (24, 135, 7)
BLUE = (43, 94, 214)
# Define the equation of the line (y = mx + b)

rise = 0

run = 1
#m = (rise/run)/2
b = 0



rise_choosen = False

unfinshed = True

slope_gotten = False

run_gotten = False

clock = pygame.time.Clock()



# Loop until the user clicks the close button
done = False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                unfinshed = True
                rise_choosen = False
                run_gotten = False
                slope_gotten = False

    if unfinshed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        if event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_UP:
                if rise_choosen == False:
                    rise += 1
                elif run_gotten == False :
                    run += 1       
                else:
                    b += 10

            if event.key == pygame.K_DOWN:
                if rise_choosen == False:    
                        rise += -1    
                elif run_gotten == False:
                    if run >= 2:
                        run += -1
                else:
                    b += -10

            if event.key == pygame.K_RETURN:
                if rise_choosen == False:
                    rise_choosen = True
                
                elif run_gotten == False:
                        run_gotten = True
                
                else:
                    unfinshed = False
                    
                    m = (rise/run)/2
                    
                    # Define the x and y values to plot
                    
                    x_values = range(0, 800)
                    y_values = [int(m * x + b) for x in x_values]
                    slope_gotten = True
                    


        

        if rise_choosen == False:    
        
            rise_number_surface = text.render(f'Rise :{rise}',False,GREEN)
            rise_number_rect = rise_number_surface.get_rect(midtop = ((wn_x/2),(wn_y/2 + 100)))

            screen.fill(WHITE)

            screen.blit(rise_number_surface,rise_number_rect)
        
        
        elif run_gotten == False:
        
            run_number_surface = text.render(f'Run :{run}',False,GREEN)
            run_number_rect = run_number_surface.get_rect(midtop = ((wn_x/2),(wn_y/2 + 200)))

            screen.fill(WHITE)

            screen.blit(run_number_surface,run_number_rect)
            screen.blit(rise_number_surface,rise_number_rect)
        
        
        else:
            y_int_number_surface = text.render(f'y int :{b}',False,GREEN)
            y_int_number_rect = y_int_number_surface.get_rect(midtop = ((wn_x/2),(wn_y/2 + 300)))

            screen.fill(WHITE)

            screen.blit(run_number_surface,run_number_rect)
            screen.blit(rise_number_surface,rise_number_rect)
            screen.blit(y_int_number_surface,y_int_number_rect)

        #the random image
        screen.blit(image_surface,image_rect)


    if slope_gotten == True:
       
        # Color the screen 
        screen.fill(BLACK)


        # Draw the orgin point

        pygame.draw.aaline(screen, BLUE, ((wn_x/2),0), ((wn_x/2),wn_y), 5)
        pygame.draw.aaline(screen, BLUE, (0,(wn_y/2)), (wn_x,(wn_y/2)), 5)


        # Draw the lines
        pygame.draw.aaline(screen, GREEN, ((wn_x/2), -1*b + (wn_y/2)), (wn_x, int(-1*m * wn_x + -1*b + (wn_y/2))), 5)
    
        if m >= 1: pygame.draw.aaline(screen, GREEN, ((wn_x/2), -1*b + (wn_y/2)), (0, int(m * wn_x + -1*b + (wn_y/2))), 5)
    
        else: pygame.draw.aaline(screen, GREEN, ((wn_x/2), -1*b + (wn_y/2)), (0, int(m * wn_x + -1*b + (wn_y/2))), 5) 
    
        
   

    # Update the screen
    pygame.display.flip()
    
    

    # Wait for a short period of time to control the frame rate
    clock.tick(5)

# Quit Pygame
pygame.quit()
sys.exit()