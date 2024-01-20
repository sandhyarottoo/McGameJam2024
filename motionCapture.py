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

# render the numbers for countdown
font_size = 250
font = pygame.font.SysFont(None, font_size)
numba3 = font.render('3', True, (255, 255, 255))  # White color
numba2 = font.render('2', True, (255, 255, 255))  # White color
numba1 = font.render('1', True, (255, 255, 255))  # White color

numbaDict = {1: numba1, 2: numba2, 3: numba3}


### STARTING GAME LOOP ###

filepath = os.path.dirname(os.path.realpath(__file__)) + '/capturedAnimations/test.txt'
file = open(filepath, 'w')

capture = False
initiateCountdown = False
drawRed = False
prevTime = pygame.time.get_ticks()
secondCount = 3

running = True
while running:

    time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                initiateCountdown = True
            
    mouseX, mouseY = pygame.mouse.get_pos()

    screen.fill((0,0,0))

    if initiateCountdown and secondCount > 0:

        screen.blit(numbaDict[secondCount], (WIDTH/2, HEIGHT/2))
        if time - prevTime > 1000:
            secondCount -= 1
            prevTime = time
        
    if secondCount == 0:
        secondCount = -1
        initiateCountdown = False
        capture = True
        drawRed = True

    if drawRed:
        pygame.draw.rect(screen, (255,0,0), (50, 50, 100, 100))
    
    

    if capture:





    if capture:
        


        
    
    
    for group in groupOfGroups:
        group.update(dt)
        group.draw(screen)


    pygame.display.flip()
        
file.close()

pygame.quit()
sys.exit()