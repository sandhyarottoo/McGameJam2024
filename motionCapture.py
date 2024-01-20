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

file = os.path.dirname(os.path.realpath(__file__)) + '/capturedAnimations/test.txt'
capture = False

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    # OBSTACLE SECTION

    if capture:
        mouseX, mouseY = pygame.mouse.get_pos()


        
    screen.fill((0,0,0))
    
    for group in groupOfGroups:
        group.update(dt)
        group.draw(screen)


    pygame.display.flip()
        

# initializing menu
menu = pygame_menu.Menu("Main Menu", WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_BLUE)

menu.add.button('Play', start_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)

pygame.quit()
sys.exit()