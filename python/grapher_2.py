import pygame

import sys

# Set up Pygame
pygame.init()
wn_x = 800
wn_y = 800 #min of 700
size = (wn_x, wn_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Linear Line Graph")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (24, 135, 7)
BLUE = (43, 94, 214)


# Fonts
text = pygame.font.Font('fonts/data-latin.ttf',50)
small_text = pygame.font.Font('fonts/data-latin.ttf',15)
# Define a new surface and rect

image_surface = pygame.image.load('images/man from the poster transparent.png')
image_rect = image_surface.get_rect(midtop = ((wn_x/2),(wn_y/2 - 300)))

# Define a new surface for text

instructions = small_text.render('use the up and down arow to select a number press enter if you want to go back press Esc', False, GREEN )
instructions_rect = instructions.get_rect(midtop =((wn_x/2) , 100))

# Define a funtion 

def mouse_input_teller():
    if pygame.mouse.get_pos()[0] < wn_x and pygame.mouse.get_pos()[0] > 0 and pygame.mouse.get_pos()[1] < wn_y and pygame.mouse.get_pos()[1] > 0:
        return True
    else:
        return False





# Define the equation of the line (y = mx + b)
# m = (rise/run)/2
# run != 0
rise = 0

run = 1

b = 0

mouse_is_down = False

mouse_input = False

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


        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_is_down = True
            starting_point = pygame.mouse.get_pos()
        else:
            mouse_is_down = False

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
        
            rise_number_surface = text.render(f'-> Rise :{rise}',False,GREEN)
            rise_number_rect = rise_number_surface.get_rect(midtop = ((wn_x/2),(wn_y/2 + 100)))
            run_number_surface = text.render(f'Run :{run}',False,GREEN)
            run_number_rect = run_number_surface.get_rect(midtop = ((wn_x/2),(wn_y/2 + 200)))
            y_int_number_surface = text.render(f'y int :{b}',False,GREEN)
            y_int_number_rect = y_int_number_surface.get_rect(midtop = ((wn_x/2),(wn_y/2 + 300)))


            screen.fill(WHITE)

            screen.blit(rise_number_surface,rise_number_rect)
            screen.blit(run_number_surface,run_number_rect)
            screen.blit(y_int_number_surface,y_int_number_rect)
        
        elif run_gotten == False:
            
            rise_number_surface = text.render(f'Rise :{rise}',False,GREEN)
            rise_number_rect = rise_number_surface.get_rect(midtop = ((wn_x/2),(wn_y/2 + 100)))
            run_number_surface = text.render(f'-> Run :{run}',False,GREEN)
            run_number_rect = run_number_surface.get_rect(midtop = ((wn_x/2),(wn_y/2 + 200)))
            y_int_number_surface = text.render(f'y int :{b}',False,GREEN)
            y_int_number_rect = y_int_number_surface.get_rect(midtop = ((wn_x/2),(wn_y/2 + 300)))

            screen.fill(WHITE)

            screen.blit(run_number_surface,run_number_rect)
            screen.blit(rise_number_surface,rise_number_rect)
            screen.blit(y_int_number_surface,y_int_number_rect)
        
        else:
            
            run_number_surface = text.render(f'Run :{run}',False,GREEN)
            run_number_rect = run_number_surface.get_rect(midtop = ((wn_x/2),(wn_y/2 + 200)))
            y_int_number_surface = text.render(f'-> y int :{b}',False,GREEN)
            y_int_number_rect = y_int_number_surface.get_rect(midtop = ((wn_x/2),(wn_y/2 + 300)))
            
            screen.fill(WHITE)

            screen.blit(run_number_surface,run_number_rect)
            screen.blit(rise_number_surface,rise_number_rect)
            screen.blit(y_int_number_surface,y_int_number_rect)

        #the random image
        screen.blit(image_surface,image_rect)
        screen.blit(instructions,instructions_rect)

    if slope_gotten == True:
       
        # Color the screen 
        screen.fill(BLACK)


        # Draw the orgin point

        pygame.draw.aaline(screen, BLUE, ((wn_x/2),0), ((wn_x/2),wn_y), 5)
        pygame.draw.aaline(screen, BLUE, (0,(wn_y/2)), (wn_x,(wn_y/2)), 5)


        # Draw the lines
        if mouse_input_teller and mouse_is_down:
            pygame.draw.aaline(screen, GREEN, pygame.mouse.get_pos(), (wn_x, int(-1*m * wn_x + -1*b + (wn_y/2))), 5)
        
            if m >= 1: pygame.draw.aaline(screen, GREEN, pygame.mouse.get_pos(), (0, int(m * wn_x + -1*b + (wn_y/2))), 5)
        
            else: pygame.draw.aaline(screen, GREEN, pygame.mouse.get_pos(), (0, int(m * wn_x + -1*b + (wn_y/2))), 5) 
        
        else:
            pygame.draw.aaline(screen, GREEN, ((wn_x/2), -1*b + (wn_y/2)), (wn_x, int(-1*m * wn_x + -1*b + (wn_y/2))), 5)
        
            if m >= 1: pygame.draw.aaline(screen, GREEN, ((wn_x/2), -1*b + (wn_y/2)), (0, int(m * wn_x + -1*b + (wn_y/2))), 5)
        
            else: pygame.draw.aaline(screen, GREEN, ((wn_x/2), -1*b + (wn_y/2)), (0, int(m * wn_x + -1*b + (wn_y/2))), 5) 
        
        #add the use of vectors to make line bounce

    # Update the screen
    pygame.display.flip()
    
    

    # Wait for a short period of time to control the frame rate
    if mouse_input_teller() and slope_gotten:
        clock.tick(60)
    else:
        clock.tick(5)

# Quit Pygame
pygame.quit()
sys.exit()