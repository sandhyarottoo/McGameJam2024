import pygame
import pygame_menu # install this using ==> pip install pygame-menu -U
import numpy as np
from globalVars import getVars
from ObjectClasses.BackgroundObject import BackgroundObject
from ObjectClasses.Contraption import Contraption
import ObjectClasses.player as player
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

catImage = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/cat.png').convert_alpha()
catImage = pygame.transform.scale(catImage, (100, 100))

character = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/physicist_v1.png').convert_alpha()
character = pygame.transform.scale(character, (100, 100))
# cat = BackgroundObject(catImage)

# backgroundGroup = pygame.sprite.Group()
# groupOfGroups.append(backgroundGroup)
# backgroundGroup.add(cat)

characterGroup = pygame.sprite.Group()
groupOfGroups.append(characterGroup)
contraption = Contraption(catImage)
characterGroup.add(contraption)

groundObstacles = pygame.sprite.Group()
groupOfGroups.append(groundObstacles)

platforms = pygame.sprite.Group()
groupOfGroups.append(platforms)

physicist = helpers.createPlayer()
players = pygame.sprite.Group()
players.add(physicist)

### STARTING GAME LOOP ###


def start_game():

    prevGroundObsTime = pygame.time.get_ticks()
    groundObstacleInterval = 4000

    platformTime = 0
    platformsToAdd = 0

    running = True
    while running:

        time = pygame.time.get_ticks()
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # OBSTACLE SECTION

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

        keys = pygame.key.get_pressed()
        players.update(events, keys, platforms, groundObstacles)
        players.draw(screen)
        
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