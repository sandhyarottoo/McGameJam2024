import pygame 
from globalVars import getVars
import os

WIDTH, HEIGHT = getVars(['width', 'height'])

class BackgroundObject(pygame.sprite.Sprite):

    def __init__(self, image, speed, position):
        super().__init__()

        self.pos = position
        self.vel = pygame.Vector2(-speed, 0)

        #scale image to the size of screen
        image = pygame.transform.scale(image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x, self.pos.y)
    
    def update(self, dt):

        # make it appear on opposite side when it passes the screen 
        if self.pos.x + self.image.get_width()/2 < 0:
            self.pos.x = WIDTH + self.image.get_width()/2

        self.pos += self.vel*dt
        self.rect.center = (self.pos.x, self.pos.y)

catImage = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/cat.png').convert_alpha()
catBack = BackgroundObject(catImage, 10, pygame.Vector2(catImage.get_width()/2, catImage.get_height()/2))