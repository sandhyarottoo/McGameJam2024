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

# catImage = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/cat.png').convert_alpha()
# catImage = pygame.transform.scale(catImage, (100, 100))
# cat = BackgroundObject(catImage)

# backgroundGroup = pygame.sprite.Group()
# groupOfGroups.append(backgroundGroup)
# backgroundGroup.add(cat)

groundObstacles = pygame.sprite.Group()
groupOfGroups.append(groundObstacles)

platforms = pygame.sprite.Group()
groupOfGroups.append(platforms)

### STARTING GAME LOOP ###


def start_game():

    prevGroundObsTime = pygame.time.get_ticks()
    groundObstacleInterval = 4000

    platformTime = 0
    platformsToAdd = 0

    running = True
    while running:

        time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False


        if time - prevGroundObsTime > groundObstacleInterval:
            prevGroundObsTime = time
            groundObstacles.add(helpers.createGroundObstacle())
            platformTime = time
            platformsToAdd = 3

        if platformsToAdd > 0:
            if time - platformTime > groundObstacleInterval/5:
                platformTime = time
                if platformsToAdd == 3:
                    platforms.add(helpers.createPlatform(low=True))
                else:
                    platforms.add(helpers.createPlatform(low=False))
                
                platformsToAdd -= 1

            
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