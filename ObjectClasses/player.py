import pygame
import numpy as np
import os
from globalVars import getVars
import audioFunctions

PLAYERXVEL = getVars(['playervelocity'])[0]

WIDTH, HEIGHT, dt, PLAYERYVEL, playerheight, playerwidth, g = getVars(['width', 'height', 'dt','jumpvel', 'playerheight', 'playerwidth', 'g'])

class Player(pygame.sprite.Sprite):
    def __init__(self,images):
        super().__init__()
        for i, img in enumerate(images):
            images[i] = pygame.transform.scale(img, (playerwidth, playerheight))
        
        self.images = images
        self.image = images[0]
        self.pos = pygame.Vector2(0, HEIGHT - 10 - playerheight/2)
        self.vel = pygame.Vector2(0,0)
        self.acc = pygame.Vector2(0,0)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x, self.pos.y)
        self.mass = 10
        self.charge = 1
        self.jumping = False
        self.health = 3
        self.respawn = False
        self.moveType = 'running'
        self.moveFreely = False
        
        # for animation
        self.dtime= 0
        self.index = 0

        # add sound delay for running
        self.soundTime = 0

    def update(self, events, keys, platforms, obstacles,bullets):
        # if not self.jumping and self.soundTime > 100*dt:
        #     audioFunctions.playRun()
        #     self.soundTime = 0
        # self.soundTime += dt
        
        if self.moveType == 'running':
            if self.dtime >  100*dt: 
                self.image = self.images[self.index]
                self.index += 1
                self.dtime = 0
                if self.index > 1:
                    self.index = 0
                
            self.dtime += dt
            
            #treat landing on the ground
            if self.pos.y + playerheight/2 > HEIGHT - 10:
                self.vel.x *= 0.9
                self.pos.y = HEIGHT - 10 - playerheight/2
                self.vel.y = 0
                self.jumping = False
            
            #treat the platform collisions
            for platform in platforms:
                self.landing(platform, dt)
            #treat the obstacle collisions
            for obstacle in obstacles:
                self.collision(obstacle, dt)

            for bullet in bullets: 
                if self.enemyCollision(bullet):
                    self.health -= 1
                    self.respawn = True
                    audioFunctions.playHurt()

            if self.respawn:
                self.pos = pygame.Vector2(WIDTH/2, HEIGHT - 10 - playerheight/2)
                self.vel = pygame.Vector2(10,0)
                self.respawn = False

            #jump, hit the key once
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.jumping:
                        self.vel.y += -300
                        self.jumping = True
                        audioFunctions.playJump()
            
            
            #left and right motion, continuous
            if keys[pygame.K_RIGHT] and self.pos.x <= 2*WIDTH/3:
                self.pos.x += PLAYERXVEL
            if keys[pygame.K_LEFT]:
                self.pos.x -= PLAYERXVEL
            

            #accelerate with forces
            self.acc = self.applyForces(['gravity', 'electricity'], bullets)/self.mass
            self.vel += self.acc*dt
            self.pos += self.vel*dt
            

        elif self.moveType == "boss cutscene":
            #treat landing on the ground
            if self.pos.y + playerheight/2 > HEIGHT - 10:
                self.vel.x *= 0.9
                self.pos.y = HEIGHT - 10 - playerheight/2
                self.vel.y = 0
                self.jumping = False

            self.pos.x += 2*(WIDTH/4 - self.pos.x)*dt

            #accelerate with forces
            self.acc = self.applyForces(['gravity', 'electricity'], bullets)/self.mass
            self.vel += self.acc*dt
            self.pos += self.vel*dt
        
        elif self.moveType == 'flying': 
            if not self.moveFreely:      
                self.pos.y += 3*(HEIGHT/2 - self.pos.y)*dt
                if abs(HEIGHT/2 - self.pos.y) < 3:
                    self.moveFreely = True
            
            if self.rect.right > WIDTH:
                self.pos.x = WIDTH - self.image.get_width()/2
                self.vel.x = 0
            if self.rect.left < 0:
                self.pos.x = 0 + self.image.get_width()/2
                self.vel.x = 0
            if self.rect.top < 0:
                self.pos.y = 0 + self.image.get_height()/2  
                self.vel.y = 0
            if self.rect.bottom > HEIGHT:
                self.pos.y = HEIGHT - self.image.get_height()/2
                self.vel.y = 0
            
            for bullet in bullets: 
                if self.enemyCollision(bullet):
                    audioFunctions.playHurt()
                    self.health -= 1
                    self.respawn = True
            if self.respawn:
                self.pos = pygame.Vector2(WIDTH/2, HEIGHT - 10 - playerheight/2)
                self.vel = pygame.Vector2(10,0)
                self.respawn = False
            
            mult = 1.5
            if keys[pygame.K_RIGHT]:
                self.vel.x += mult*PLAYERXVEL
            if keys[pygame.K_LEFT]:
                self.vel.x -= mult*PLAYERXVEL
            if keys[pygame.K_UP]:
                self.vel.y -= mult*PLAYERXVEL
            if keys[pygame.K_DOWN]:
                self.vel.y += mult*PLAYERXVEL
            
            self.acc = self.applyForces(['electricity'], bullets)/self.mass
            self.vel += self.acc*dt
            self.pos += self.vel*dt
            
            
        self.rect.center = (self.pos.x, self.pos.y)
        

    def landing(self, platform, dt):
        #for landing on a platform
        if pygame.sprite.collide_mask(self, platform) and self.vel.y > 0 and (self.pos.y + playerheight/2) < platform.rect.top + 10 :
            newpos = platform.rect.top - playerheight/2
            self.vel.x = platform.vel.x
            self.pos.y = newpos
            self.vel.y = 0
            
            self.jumping = False

    def collision(self,obstacle, dt):
        #for knocking into an obstacle
        if pygame.sprite.collide_mask(self,obstacle):
            # sides
            if (self.pos.y + playerheight/2) > obstacle.rect.top + 5:
                if self.pos.x < obstacle.rect.left:
                    self.pos.x = obstacle.rect.left - playerwidth/2
                else:
                    self.pos.x = obstacle.rect.right + playerwidth/2

            elif self.vel.y > 0:
                self.pos.y = obstacle.rect.top - playerheight/2
                self.vel.x = obstacle.vel.x
                self.vel.y = 0
                self.jumping = False
        

    def enemyCollision(self,enemy):
        if pygame.sprite.collide_mask(self,enemy):
            return True

        

    def applyForces(self, listofforces, bullets):
        
        force = pygame.Vector2(0, 0)

        if 'gravity' in listofforces:
            force += pygame.Vector2(0, self.mass*g)
    
        if 'electricity' in listofforces:
            for bullet in bullets:
                r = bullet.pos-self.pos
                bulletCharge = bullet.charge
                abs_r_sq = np.sqrt(r.x**2 + r.y**2)
                force += (900000000*bulletCharge*self.charge/(abs_r_sq)**3)*r.normalize()
    
            
        return force



class PlayerHealth(pygame.sprite.Sprite):
    heartcounter = 0
    def __init__(self,image,posx,posy):
        super().__init__()
        self.image = pygame.transform.scale(image, (20, 20))
        self.pos = pygame.Vector2(posx,posy)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x, self.pos.y)
        PlayerHealth.heartcounter += 1
        self.number = PlayerHealth.heartcounter

    def update(self,players):
        for player in players:
            if self.number == 3:
                if player.health == 2:
                    self.kill()
            elif self.number == 2:
                if player.health == 1:
                    self.kill()
            elif self.number == 1:
                if player.health == 0:
                    self.kill()
                    #player.kill()




