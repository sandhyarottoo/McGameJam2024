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
        self.rect.center = (0,HEIGHT-100)
        self.mass = 10
        self.charge = 1


    def update(self,events,keys,platforms,obstacles):

        #jump, hit the key once
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.vel.y = -200


        #accelerate with forces
        self.acc = self.applyForces(['gravity'])
        self.vel += self.acc
        self.rect.x += self.vel.x*dt
        self.rect.y += self.vel.y*dt
        #treat the platform collisions
        for platform in platforms:
            self.landing(platform)
        #treat the obstacle collisions
        for obstacle in obstacles:
            self.collision(obstacle)
        
        #treat landing on the ground
        ground = pygame.Rect(0, HEIGHT - 10, WIDTH, 10)
        if ground.colliderect(self.rect):
            self.rect.y = ground.top-playerheight/2
            self.vel.y = 0

        #left and right motion, continuous
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYERXVEL
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYERXVEL



            
                        



    def landing(self,platform):
        #for landing on a platform
        if pygame.sprite.collide_mask(self,platform) and self.vel.y > 0:
            newpos = platform.rect.top - playerheight
            self.rect.y = newpos
            self.vel.y = 0

    def collision(self,obstacle):
        #for knocking into an obstacle
        if pygame.sprite.collide_mask(self,obstacle):
            self.vel.x *=-1


    def enemyCollision(self,enemy):

        if pygame.sprite.collide_mask(self,enemy):
            return True
        

    def applyForces(self,listofforces):
        #get accelerations
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


