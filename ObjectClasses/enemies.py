import pygame
import numpy as np
import os
from globalVars import getVars
from ObjectClasses.player import Player as player

permittivity = 10

# darknessImage = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/darkness.png').convert_alpha()
# darknessImage = pygame.transform.scale(darknessImage, (2000, 2000))


WIDTH, HEIGHT, dt, PLAYERXVEL,PLAYERYVEL = getVars(['width', 'height', 'dt','playervelocity','jumpvel'])
#imagepos = positive charge
#imageneg = negative charge

# 1 <3 peeny

class ChargeBullet(pygame.sprite.Sprite):
    def __init__(self,sign,imagepos,imageneg,xpos,ypos, mode):
        super().__init__()
        #sign has to be 1 or -1
        self.charge = sign*permittivity
        self.mode = mode

        if sign == 1:
            image = imagepos
        elif sign == -1:
            image = imageneg
        self.image = image
        self.pos = pygame.Vector2(xpos,ypos)
        if self.mode == 'level':
            self.vel = pygame.Vector2(-300,0)
        if self.mode == 'bossfight':
            angle = np.random.random()*-np.pi
            self.vel = 200*pygame.Vector2(np.cos(angle),np.sin(angle))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x, self.pos.y)

    def update(self,dt):
        self.pos += self.vel*dt
        self.rect.center = (self.pos.x, self.pos.y)

        right = self.rect.right
        left = self.rect.left
        bottom = self.rect.bottom

        if  right < 0 or left > WIDTH or bottom < 0:
            self.kill()

    def getChargePos(self):
        return self.rect
    

class Laser(pygame.sprite.Sprite):

    def __init__(self, image, posx,posy,mode):
        super().__init__()
        image = pygame.transform.scale(image, (WIDTH-150, 60))
        self.image = image
        self.rect = self.image.get_rect()
        if mode == 'level':
            self.pos = pygame.Vector2(0, np.random.random()*HEIGHT/2)
        if mode == 'bossfight':
            self.pos = (posx,posy)
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.image.get_rect(center=(posx,posy))
        self.colour = (0,0,0)

        self.rect.left = (self.pos.x,self.pos.y)    

    def update(self,player,screen,time,dt):
        initialtime = time
        if pygame.time.Clock.get_time() - initialtime > 2500:
            self.kill()

    def hitPlayer(self,player,laserwarning):
        if pygame.sprite.collide_mask(self,player):
            self.kill()
            laserwarning.kill()



class LaserWarning(pygame.sprite.Sprite):
    def __init__(self,radius,laser):
        self.image = pygame.Surface((radius,radius))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (laser.pos.x,laser.pos.y)
        self.producedLaser = False



            




