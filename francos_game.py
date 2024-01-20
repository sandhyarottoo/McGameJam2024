import pygame
import pygame_menu # install this using ==> pip install pygame-menu -U
import numpy as np
from globalVars import getVars
from BackgroundObject import BackgroundObject
import helperFunctions as helpers
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

groundObstacles = pygame.sprite.Group()

### STARTING GAME LOOP ###


def start_game():

    prevTime = pygame.time.get_ticks()
    groundObstacleInterval = 2000

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            elif event.type == pygame.K_ESCAPE or event.type == pygame.K_DELETE:
                running = False

        if pygame.time.get_ticks() - prevTime > groundObstacleInterval:
            prevTime = pygame.time.get_ticks()
            groundObstacles.add(helpers.createGroundObstacle())

            

        screen.fill((0,0,0))

        backgroundGroup.update(dt)
        backgroundGroup.draw(screen)

        groundObstacles.update(dt)
        groundObstacles.draw(screen)


        pygame.display.flip()
        

# initializing menu
menu = pygame_menu.Menu("Main Menu", WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_BLUE)

menu.add.button('Play', start_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)

pygame.quit()
sys.exit()