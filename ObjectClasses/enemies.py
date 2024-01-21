import pygame
import numpy as np
import os
from globalVars import getVars
import ObjectClasses.player as player

WIDTH, HEIGHT, dt, PLAYERXVEL,PLAYERYVEL = getVars(['width', 'height', 'dt','playervelocity','jumpvel'])
#imagepos = positive charge
#imageneg = negative charge

class ChargeBullet(pygame.sprite.Sprite):
    def __init__(self,sign,imagepos,imageneg, xpos, ypos,mode):
        super().__init__()

        permittivity = 10
        #sign has to be 1 or -1
        self.charge = sign*permittivity

        if sign == 1:
            image = imagepos
        elif sign == -1:
            image = imageneg

        self.image = image
        self.pos = pygame.Vector2(xpos, ypos)
        if mode == 'level':    
            self.vel = pygame.Vector2(-300,0)
        if mode == 'bossfight':
            #generate a random angle between 0 and pi
            angle = np.random.random()*np.pi
            self.vel = 300*pygame.Vector2(np.cos(angle),np.sin(angle))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x, self.pos.y)

    def update(self,dt):
        self.pos.x += self.vel.x*dt

        if self.pos.x + self.image.get_width()/2 < 0:
            self.kill()

        self.rect.center = (self.pos.x, self.pos.y)
    


