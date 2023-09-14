import pygame 

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, color, display_surface):
        super().__init__()
        if color == 'rock':
            self.image = pygame.image.load('images/crapygrass_tile_80x80.png')
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

    def switch_texture(self, texture_index):
        if self.color != 'blue'or self.color != 'ladder':
            if texture_index == 1:
                self.image = pygame.image.load('images/rock_tile_80x80.png')
                self.collision = True
            if texture_index == 2:
                self.image = pygame.image.load('images/face_tile_80x80.png')
                self.collision = True


        pass
    
    def update(self, x_shift):
        pygame.draw.line(self.display_surface, 'red', self.pos, (self.pos[0]+40, self.pos[1]-40))
       

        self.rect.x += x_shift
        self.pos = (self.rect.x, self.rect.y)
        None