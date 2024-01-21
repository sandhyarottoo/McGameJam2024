import pygame
import numpy as np
from globalVars import getVars


# importing global variables
WIDTH, HEIGHT, dt, g = getVars(['width', 'height', 'dt', 'g'])

# creating class
class Contraption(pygame.sprite.Sprite):
    '''
    Class for the contraption. 
    '''

    def __init__(self, image):
        super().__init__()

        self.xtimeParam = 0
        self.ytimeParam = 0
        self.anchorPoint = pygame.Vector2(19/20*WIDTH - 8, 6/10*HEIGHT)
        self.amplitude = 25
        self.pos = pygame.Vector2(19/20*WIDTH, 4/10*HEIGHT)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)
        
        self.moveType = "hovering"
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x, self.pos.y)
    
    
    def update(self, dt):
        
        if self.moveType == "hovering":
            
            self.xtimeParam += dt
            self.ytimeParam += dt

            if self.xtimeParam > 2*np.pi:
                self.xtimeParam = 0
            if self.ytimeParam > np.pi:
                self.ytimeParam = 0

            self.pos.x = self.anchorPoint.x + (self.amplitude/2)*np.sin(self.xtimeParam)
            self.pos.y = self.anchorPoint.y + (3*self.amplitude)*np.sin(2*self.ytimeParam)

        
        if self.moveType == "centering":
            self.acc.y = g
            self.vel += self.acc*dt
            self.pos += self.vel*dt

            self.pos.x += (WIDTH/2 - self.pos.x)*dt
            
            if self.pos.y + self.image.get_height()/2 > HEIGHT - 10:
                self.pos.y = HEIGHT - 10 - self.image.get_height()/2
                self.vel.y = 0
            
            if abs(self.pos.x - WIDTH/2) < 2:
                self.vel = pygame.Vector2(0, 0)
                self.acc = pygame.Vector2(0, 0)
                self.moveType = "standing"
            
        if self.moveType == "standing":
            pass
        
        self.rect.center = (self.pos.x, self.pos.y)



        