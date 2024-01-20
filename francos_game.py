import pygame
import numpy as np
from globalVars import getVars
from BackgroundObject import BackgroundObject
import sys
import os

WIDTH, HEIGHT, dt = getVars(['width', 'height', 'dt'])

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

### OBJECT SETUP ###

catImage = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/cat.png').convert_alpha()
catImage = pygame.transform.scale(catImage, (100, 100))
cat = BackgroundObject(catImage)

backgroundGroup = pygame.sprite.Group()
backgroundGroup.add(cat)

### STARTING GAME LOOP ###


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         bucket.vel.x -= bucket.walkSpeed
        #     if event.key == pygame.K_RIGHT:
        #         bucket.vel.x += bucket.walkSpeed
        #     if event.key == pygame.K_SPACE:
        #         position, velocity = getInitialParams()
        #         ball.pos = position
        #         ball.vel = velocity
                
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT:
        #         if pygame.key.get_pressed()[pygame.K_RIGHT]:
        #             bucket.vel.x += bucket.walkSpeed
        #         else:
        #             bucket.vel.x = 0
        #     if event.key == pygame.K_RIGHT:
        #         if pygame.key.get_pressed()[pygame.K_LEFT]:
        #             bucket.vel.x -= bucket.walkSpeed
        #         else:
        #             bucket.vel.x = 0
        

    screen.fill((0,0,0))

    backgroundGroup.update(dt)
    backgroundGroup.draw(screen)


    pygame.display.flip()

pygame.quit()
sys.exit()