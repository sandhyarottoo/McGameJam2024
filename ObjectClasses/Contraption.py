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

        self.pos = pygame.Vector2(17/20*WIDTH, 3/10*HEIGHT)
        self.vel = pygame.Vector2(30, 40)
        
        
        self.moveType = "hovering"
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x, self.pos.y)
    
    
    def update(self, dt):
        
        if self.moveType == "hovering":
            
            self.pos += self.vel*dt
            self.rect.center = (self.pos.x, self.pos.y)
            
            if self.pos.x > 16/20*WIDTH or self.pos.x < 19/20*WIDTH:
                self.vel.x *= -1
            if self.pos.y > 4/10*HEIGHT or self.pos.y < 3/10*HEIGHT:
                self.vel.y *= -1