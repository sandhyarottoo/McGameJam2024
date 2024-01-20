import pygame
import numpy as np
import os
from globalVars import getVars

WIDTH, HEIGHT, dt, PLAYERXVEL,PLAYERYVEL,playerheight,playerwidth = getVars(['width', 'height', 'dt','playervelocity','jumpvel','playerheight','playerwidth'])

class Player(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        ogImage = pygame.image.load(image)
        self.image = pygame.transform.scale(ogImage, (playerwidth, playerheight))

        self.pos = pygame.Vector2(0, HEIGHT - 10 - playerheight/2)
        self.vel = pygame.Vector2(0,0)
        self.acc = pygame.Vector2(0,0)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x, self.pos.y)
        self.mass = 10
        self.charge = 1
        self.jumping = False


    def update(self, events, keys, platforms, obstacles):
        
        #treat landing on the ground
        if self.pos.y + playerheight/2 > HEIGHT - 10:
            self.pos.y = HEIGHT - 10 - playerheight/2
            self.vel.y = 0
            self.jumping = False

        #jump, hit the key once
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.jumping:
                    self.vel.y += -300
                    self.jumping = True

        #left and right motion, continuous
        if keys[pygame.K_RIGHT]:
            self.pos.x += PLAYERXVEL
        if keys[pygame.K_LEFT]:
            self.pos.x -= PLAYERXVEL
        
        #accelerate with forces
        self.acc = self.applyForces(['gravity'])/self.mass
        self.vel += self.acc*dt
        self.pos += self.vel*dt
        
        #treat the platform collisions
        for platform in platforms:
            self.landing(platform, dt)
        #treat the obstacle collisions
        for obstacle in obstacles:
            self.collision(obstacle, dt)
        
        self.rect.center = (self.pos.x, self.pos.y)
        


    def landing(self, platform, dt):
        #for landing on a platform
        if pygame.sprite.collide_mask(self, platform) and self.vel.y > 0 and (self.pos.y + playerheight/2) < platform.rect.top + 10 :
            newpos = platform.rect.top - playerheight/2
            self.pos.y = newpos
            self.vel.y = 0
            self.pos.x += platform.vel.x*dt
            self.jumping = False

    def collision(self,obstacle, dt):
        #for knocking into an obstacle
        if pygame.sprite.collide_mask(self,obstacle):
            if self.vel.x >= 0:
                self.pos.x = obstacle.rect.left - playerwidth/2
            else:
                self.pos.x = obstacle.rect.right + playerwidth/2
        
            
            


    def enemyCollision(self,enemy):

        if pygame.sprite.collide_mask(self,enemy):
            return True
        

    def applyForces(self,listofforces):
        #get accelerations
        
        force = pygame.Vector2(0, 0)

        if 'gravity' in listofforces:
            g = 200
            force += pygame.Vector2(0, self.mass*g)
    
        #if 'electricity' in listofforces:


        return force


    #if force == 'electric':

# def infinitePlane(player):
#     #for an infinite charged plane on the ground


