
import numpy as np
import pygame
import sys
import os
import pygame_menu
from globalVars import getVars
from ObjectClasses.BackgroundObject import BackgroundObject
import ObjectClasses.player as player
import ObjectClasses.Obstacles as Obstacles
import helperFunctions as helpers

path = os.getcwd() + '/media/cat.png'
print(path)

WIDTH, HEIGHT, dt, PLAYERXVEL,PLAYERYVEL = getVars(['width', 'height', 'dt','playervelocity','jumpvel'])



### OBJECT SETUP ###

      

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

groupOfGroups = []
groundObstacles = pygame.sprite.Group()
groupOfGroups.append(groundObstacles)

platforms = pygame.sprite.Group()
groupOfGroups.append(platforms)

player = player.Player(path)
players = pygame.sprite.Group()
players.add(player)

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
        #screen.blit(player.image,player.rect)
        keys = pygame.key.get_pressed()
        player.update(events,keys,platforms,groundObstacles)
        players.draw(screen)
        
        for group in groupOfGroups:
            group.update(dt)
            group.draw(screen)        

        pygame.display.flip()


menu = pygame_menu.Menu("Main Menu", WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_BLUE)

menu.add.button('Play', start_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)