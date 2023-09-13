import pygame 

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, color, display_surface):
        super().__init__()
        if color == 'rock':
            self.image = pygame.image.load('images/rock_tile_80x80.png')
            self.collision = True
                
        elif color == 'ladder':
            self.image = pygame.image.load('images/face_tile_80x80.png')
            self.collision = True
        
        else:
            
            self.image = pygame.Surface((size,size))
            self.image.fill(color)
            self.collision = False
            pass

        self.rect = self.image.get_rect(topleft = pos)
        self.color = color
        self.display_surface = display_surface
        self.pos = pos

        None
        
        pass
    
    def update(self, x_shift):
        #outlines
        #if self.color == 'orange':
        #    pygame.draw.rect(self.display_surface, (230,170,200), self.rect, width = 2)


        self.rect.x += x_shift
        None