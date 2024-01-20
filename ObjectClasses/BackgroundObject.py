import pygame 
from globalVars import getVars

WIDTH, HEIGHT = getVars(['width', 'height'])

class BackgroundObject(pygame.sprite.Sprite):
    '''
    Should be provided with an image when created.
    '''

    def __init__(self, image, speed, position):
        super().__init__()

        self.pos = position
        self.vel = pygame.Vector2(-speed, 0)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x, self.pos.y)
    
    def update(self, dt):

        # make it appear on opposite side when it passes the screen 
        if self.pos.x + self.image.get_width()/2 < 0:
            self.pos.x = WIDTH + self.image.get_width()/2

        self.pos += self.vel*dt
        self.rect.center = (self.pos.x, self.pos.y)