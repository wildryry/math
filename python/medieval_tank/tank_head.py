import pygame


class Head1(pygame.sprite.Sprite):
    def __init__(self, tank_pos):
        super().__init__()
        self.image = pygame.image.load('images/tank_head1.png')
        self.rect = self.image.get_rect(center = tank_pos)
        self.rect.y += -30

    def update(self, tank_pos):
        self.rect.center = tank_pos
        self.rect.y += -30
        
        pass

    def draw(self, display):
        display.blit(self.image, self.rect)
        print(self.rect)
        pass