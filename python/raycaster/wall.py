
import pygame 

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, size, display_surface):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('green')
        self.rect = self.image.get_rect(topleft = pos)
        self.display_surface = display_surface
        None
    
    def update(self, x_shift):
        #if self.color == 'orange':
        #    pygame.draw.rect(self.display_surface, (230,170,200), self.rect, width = 2)
        #self.rect.x += x_shift
        None