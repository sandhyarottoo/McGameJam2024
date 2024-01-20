import pygame 
from globalVars import getVars
import os

WIDTH, HEIGHT = getVars(['width', 'height'])

class BackgroundObject(pygame.sprite.Sprite):
    '''
    Should be provided with an image when created.
    '''

    def __init__(self, image):
        super().__init__()

        self.pos = pygame.Vector2(WIDTH/2, HEIGHT/3)
        self.vel = pygame.Vector2(-90, 0)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x, self.pos.y)
    
    def update(self, dt):

        # make it appear on opposite side when it passes the screen 
        if self.pos.x + self.image.get_width()/2 < 0:
            self.pos.x = WIDTH + self.image.get_width()/2

        self.pos += self.vel*dt
        self.rect.center = (self.pos.x, self.pos.y)


class TrueBackgroundObject(pygame.sprite.Sprite):

    def __init__(self, image, speed, backgroundGroup):
        super().__init__()

        self.pos = pygame.Vector2(WIDTH, HEIGHT/2)
        self.vel = pygame.Vector2(-speed, 0)

        #scale image to the size of screen and produce duplicate image
        image = pygame.transform.scale(image, (2*WIDTH, HEIGHT))
        self.image = image

        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x, self.pos.y)
        backgroundGroup.add(self.image)
    
    def update(self, dt):

        # make it appear on opposite side when it passes the screen 
        if self.pos.x + self.image.get_width() <= 0:
            self.pos.x = WIDTH + self.image.get_width()

        self.pos += self.vel*dt
        self.rect.center = (self.pos.x, self.pos.y)
        #test comment
