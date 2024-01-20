import pygame
import pygame_menu # install this using ==> pip install pygame-menu -U
import numpy as np
from globalVars import getVars
from ObjectClasses.BackgroundObject import BackgroundObject
from ObjectClasses.Contraption import Contraption
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
cat = BackgroundObject(catImage)


characterGroup = pygame.sprite.Group()
groupOfGroups.append(characterGroup)
contraption = Contraption(catImage)
characterGroup.add(contraption)


backgroundGroup = pygame.sprite.Group()
groupOfGroups.append(backgroundGroup)
backgroundGroup.add(cat)

groundObstacles = pygame.sprite.Group()
groupOfGroups.append(groundObstacles)


### STARTING GAME LOOP ###


def start_game():

    prevTime = pygame.time.get_ticks()
    groundObstacleInterval = 2000

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        if pygame.time.get_ticks() - prevTime > groundObstacleInterval:
            prevTime = pygame.time.get_ticks()
            groundObstacles.add(helpers.createGroundObstacle())

            

        screen.fill((0,0,0))
        
        for group in groupOfGroups:
            group.update(dt)
            group.draw(screen)
            
        # contraption.update(dt)
        # contraption.draw(screen)


        pygame.display.flip()
        

# initializing menu
menu = pygame_menu.Menu("Main Menu", WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_BLUE)

menu.add.button('Play', start_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)

pygame.quit()
sys.exit()