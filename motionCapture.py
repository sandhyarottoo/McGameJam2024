import pygame
import pygame_menu # install this using ==> pip install pygame-menu -U
import numpy as np
from globalVars import getVars
from ObjectClasses.BackgroundObject import BackgroundObject
import helperFunctions as helpers
import sys
import os

WIDTH, HEIGHT, dt = getVars(['width', 'height', 'dt'])

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

### OBJECT SETUP ###

groupOfGroups = []

garfGroup = pygame.sprite.Group()
garf = helpers.createMotionCaptureModel("contraption")
garfGroup.add(garf)
groupOfGroups.append(garfGroup)

### STARTING GAME LOOP ###

filepath = os.path.dirname(os.path.realpath(__file__)) + '/capturedAnimations/test.txt'
file = open(filepath, 'w')

capture = False

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                initiateCountdown
            
    # OBSTACLE SECTION

    if capture:
        mouseX, mouseY = pygame.mouse.get_pos()


        
    screen.fill((0,0,0))
    
    for group in groupOfGroups:
        group.update(dt)
        group.draw(screen)


    pygame.display.flip()
        
file.close()

pygame.quit()
sys.exit()