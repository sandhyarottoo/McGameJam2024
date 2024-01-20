import pygame
import numpy as np
import os
from globalVars import getVars

WIDTH, HEIGHT, dt, PLAYERXVEL,PLAYERYVEL,playerheight,playerwidth = getVars(['width', 'height', 'dt','playervelocity','jumpvel','playerheight','playerwidth'])

class Player(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        ogImage = pygame.image.load(image)
        self.image = pygame.transform.scale(ogImage,(playerheight,playerwidth))
        self.vel = pygame.Vector2(0,0)
        self.acc = pygame.Vector2(0,0)
        self.rect = self.image.get_rect()
        self.mass = 10
        self.charge = 1


    def update(self,events,objects):
        #applyForces(self,'gravity')
        for object in objects:
            self.collision(object)

        
        ground = pygame.Rect(0, HEIGHT - 10, WIDTH, 10)
        if ground.colliderect(self.rect):
            self.rect.y = ground.top-playerheight/2
            self.vel.y = 0

        self.acc = self.applyForces(['gravity'])
        self.vel += self.acc
        
        self.rect.x += self.vel.x*dt
        self.rect.y += self.vel.y*dt

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.rect.x += PLAYERXVEL
                if event.key == pygame.K_LEFT:
                    self.rect.x -= PLAYERXVEL
                if event.key == pygame.K_SPACE:
                    self.rect.y -= PLAYERYVEL


    def collision(self,object):
        if pygame.sprite.collide_mask(self,object) and self.vel.y > 0:
            newpos = object.rect.top - playerheight/2
            self.rect.y = newpos
            self.vel.y = 0


    def applyForces(self,listofforces):
        mass = self.mass
        charge = self.charge
        xacc,yacc = 0,0
        if 'gravity' in listofforces:
            xacc += 0
            yacc += 10
    
        #if 'electricity' in listofforces:


        return pygame.Vector2(xacc,yacc)


    #if force == 'electric':

# def infinitePlane(player):
#     #for an infinite charged plane on the ground




