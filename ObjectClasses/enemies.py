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

    def __init__(self, image, chosenLaserLeft, isRandom, isDeadly):
        super().__init__()
        image = pygame.transform.scale(image, (WIDTH-150, 60))
        self.image = image
        self.rect = self.image.get_rect()
        self.isRandom = isRandom
        self.chosenLaserLeft = chosenLaserLeft
        self.isDeadly = isDeadly
        self.colour = (0,0,0)

        randLaserLeft = np.random.randint(0, WIDTH-60)

        if(self.isRandom):
            laserLeft = randLaserLeft

        else:
            laserLeft=chosenLaserLeft
            
        self.rect.center = (laserLeft+30, HEIGHT/2)    
        position = pygame.Vector2(self.rect.center)



    def laserActivate(self, laserLeft, isDeadly):
        powerupStartTime = pygame.time.Clock.get_time()
        rectangle = pygame.rect(10000, laserLeft, WIDTH-150, 1)

        while(pygame.time.Clock.get_time()-powerupStartTime<2500):
            thickness = int(56.3*(pygame.time.Clock.get_time()-powerupStartTime)/2500)+8*np.sin((pygame.time.Clock.get_time()-powerupStartTime)/120.39)
            rectangle = pygame.rect.update(laserLeft+30, 75, thickness, HEIGHT-150) 
            if isDeadly:
                self.colour = (255, 30, 50)
            else:
                self.colour = (50, 30, 255)

            #delete old rect
            #pygame.draw.rect(screen, colour, rectangle)
            
        if(pygame.time.Clock.get_time()-powerupStartTime>=2500):
            rectangle.kill()

            #Draw laser

            killTimeStart = pygame.time.Clock.get_time()
            while(pygame.time.Clock.get_time()-killTimeStart<2500):
                if pygame.sprite.collide_rect(player, self):
                    player.laserEffect()

            self.kill()
        
    def update(self,dt):
            self.rect = player.pos
        
    def Blind():
            darknessRect = darknessImage.get_rect()
            darknessRect.center = player.pos
            blindnessStart = pygame.time.Clock.get_time()

            while(pygame.time.Clock.get_time() - blindnessStart < 3000):
                size = size + 10
                darknessImage = pygame.transform.scale(darknessImage, (size, size))

            darknessImage.kill()
            darknessRect.kill()
            #blablablabla

        
        #In Player:
            '''
            for laser in lasers: 
            if (self.enemyCollision(laser) and laser.isDeadly):
                self.health -= 1
                self.respawn = True
                print(self.health)
            
            if (self.enemyCollision(laser) and !laser.isDeadly):
                enemies.Blind()
            
            '''


        #In Franco's Game:
            '''
            lasers = pygame.sprite.Group()
            groupOfGroups.append(lasers)
            '''


            




