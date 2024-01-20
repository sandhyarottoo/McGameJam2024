import pygame
import numpy as np
import os
import Obstacles
from globalVars import getVars

WIDTH, HEIGHT, dt, PLAYERXVEL,PLAYERYVEL = getVars(['width', 'height', 'dt','playervelocity','jumpvel'])

class Player(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        ogImage = pygame.image.load(image)
        self.image = pygame.transform.scale(ogImage,(100,100))
        self.yvelocity = PLAYERYVEL
        self.xvelocity = PLAYERXVEL
        self.acc = pygame.Vector2(0,0)
        self.rect = self.image.get_rect()
        self.mass = 10
        self.charge = 1


    def update(self,keys):
        #applyForces(self,'gravity')

        

        self.acc += self.applyForces(['gravity'])
        self.xvelocity += self.xacc*dt
        self.yvelocity += self.yaxx*dt
        self.rect.x += self.xvelocity
        self.
        
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.xvelocity*dt
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.xvelocity*dt
        if keys[pygame.K_UP]:
            self.rect.y -= self.yvelocity*dt


    def collision(self,object):
        if pygame.sprite.collide_mask(self,object) and self.yvelocity <0:
            newpos = object.rect.top
            self.rect.x = newpos
            self.yvelocity = 0


    def applyForces(self,listofforces):
        mass = self.mass
        charge = self.charge
        xacc,yacc = 0
        if 'gravity' in listofforces:
            xacc += 0
            yacc += 10
        return xacc,yacc

    #if force == 'electric':

# def infinitePlane(player):
#     #for an infinite charged plane on the ground




