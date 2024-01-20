import pygame
import numpy as np
from globalVars import getVars


# importing global variables
WIDTH, HEIGHT, dt = getVars(['width', 'height', 'dt'])

# creating class
class Contraption(pygame.sprite.Sprite):
    '''
    Class for the contraption. 
    '''

    def __init__(self, image):
        super().__init__()

        self.pos = pygame.Vector2(WIDTH/2, HEIGHT/2)
        self.vel = pygame.Vector2(0, 0)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x, self.pos.y)
    
    
    def update(self, dt):

        self.pos.x += 10*dt# 100*np.cos(1000*dt)
        self.pos.y = HEIGHT/2 #+ 100*np.sin(1000*dt)
        self.rect.center = (self.pos.x, self.pos.y)