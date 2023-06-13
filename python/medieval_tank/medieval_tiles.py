import pygame 

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, color, display_surface):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = pos)
        self.color = color
        self.display_surface = display_surface
        None
    
    def update(self, x_shift):
        if self.color == 'orange':
            pygame.draw.rect(self.display_surface, (230,170,200), self.rect, width = 2)
        self.rect.x += x_shift
        None