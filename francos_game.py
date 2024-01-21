import pygame
import pygame_menu # install this using ==> pip install pygame-menu -U
import numpy as np
from globalVars import getVars, changeValue, resetValues
from ObjectClasses.BackgroundObject import BackgroundObject
from ObjectClasses.Contraption import Contraption
import ObjectClasses.player as player
import helperFunctions as helpers
import ast
import sys
import os

WIDTH, HEIGHT, dt, g_obs_dims = getVars(['width', 'height', 'dt', 'g_obs_dims'])

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

### loading images ###

imageneg = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/Soccer_Ball.png').convert_alpha()
imagepos = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/Basketball_PNG.png').convert_alpha()
imageneg = pygame.transform.scale(imageneg, (50, 20))
imagepos = pygame.transform.scale(imagepos, (50, 20))

groundObjectImage = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/stronq_doge.png').convert_alpha()
groundObjectImage = pygame.transform.scale(groundObjectImage, g_obs_dims)

platformImage = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/lebron.jpeg').convert_alpha()
platformImage = pygame.transform.scale(platformImage, (80, 20))

playerIMGS = [pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/physicist_Run1.png').convert_alpha(),
              pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/physicist_Run2.png').convert_alpha()]

### OBJECT SETUP ###

groupOfGroups = []

catImage = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/cat.png').convert_alpha()
catImage = pygame.transform.scale(catImage, (100, 100))

character = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/physicist_v1.png').convert_alpha()
character = pygame.transform.scale(character, (100, 100))

bullets = pygame.sprite.Group()
groupOfGroups.append(bullets)

groundObstacles = pygame.sprite.Group()
groupOfGroups.append(groundObstacles)

platforms = pygame.sprite.Group()
groupOfGroups.append(platforms)

contraptionGroup = pygame.sprite.Group()
contraption = Contraption(catImage)
contraptionGroup.add(contraption)

physicist = player.Player(playerIMGS)
players = pygame.sprite.Group()
players.add(physicist)

life1,life2,life3 = helpers.createLife()
health = pygame.sprite.Group()
health.add(life1,life2,life3)

### STARTING GAME LOOP ###

def start_game():

    startTime = pygame.time.get_ticks()

    prevGroundObsTime = pygame.time.get_ticks()
    groundObstacleInterval = 6000

    platformTime = 0
    platformsToAdd = 0

    bulletTime = 0
    bulletInterval = 4000
    prevBulletTime = pygame.time.get_ticks()

    ### PART 1 ###

    running = True
    while running:

        time = pygame.time.get_ticks()
        events = pygame.event.get()

        if time - startTime > 8000:
            running = False

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # OBSTACLE SECTION

        if time - prevGroundObsTime > groundObstacleInterval:
            prevGroundObsTime = time
            groundObstacles.add(helpers.createGroundObstacle(groundObjectImage))
            platformTime = time
            platformsToAdd = 3

        if platformsToAdd > 0:
            if time - platformTime > groundObstacleInterval/4:
                platformTime = time
                if platformsToAdd == 3:
                    platforms.add(helpers.createPlatform(platformImage, low=True))
                else:
                    platforms.add(helpers.createPlatform(platformImage, low=False))
                
                platformsToAdd -= 1

        # bullets
        bulletInterval = np.random.randint(3000,4000)
        if time - prevBulletTime > bulletInterval:
            prevBulletTime = time
            bullet = helpers.createBullet(imagepos, imageneg, contraption.pos.x, contraption.pos.y)
            bullets.add(bullet)
            
        screen.fill((0,0,0))

        keys = pygame.key.get_pressed()
        players.update(events, keys, platforms, groundObstacles, bullets)
        for life in health:
            life.update(players)
        players.draw(screen)
        health.draw(screen)
        
        for group in groupOfGroups:
            group.update(dt)
            group.draw(screen)
        
        contraptionGroup.update(dt)
        contraptionGroup.draw(screen)

        pygame.display.flip()
    
    ### PART 2 ###
    
    for group in groupOfGroups:
        group.empty()
    
    with open(os.path.dirname(os.path.realpath(__file__)) + '/capturedAnimations/test.txt') as f:
        lines = f.readlines()
        listOfBossPositions = lines[0].split()
        listOfBossPositions = [ast.literal_eval(item) for item in listOfBossPositions]
        listOfBossPositions = listOfBossPositions[:-350]
        numOfBossPositions = len(listOfBossPositions)
    
    xDiff = contraption.pos.x - listOfBossPositions[0][0]
    yDiff = contraption.pos.y - listOfBossPositions[0][1]

    count = 0
    contraption.moveType = " "

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

        screen.fill((0,0,0))

        keys = pygame.key.get_pressed()
        players.update(events, keys, platforms, groundObstacles, bullets)
        players.draw(screen)
        
        for group in groupOfGroups:
            group.update(dt)
            group.draw(screen)
        
        if count < numOfBossPositions:
            contraption.pos.x = listOfBossPositions[count][0] + xDiff
            contraption.pos.y = listOfBossPositions[count][1] + yDiff
            count += 1
        else:
            contraption.moveType = "standing"

        contraptionGroup.update(dt)
        contraptionGroup.draw(screen)


        pygame.display.flip()
        

# initializing menu
menu = pygame_menu.Menu("Main Menu", WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_BLUE)

def set_sensitivity(value, sensitivity):
    changeValue('playervelocity', sensitivity)
    print(getVars())

menu.add.button('Play', start_game)
menu.add.selector('Sensitivity: ', [('Low', 1), ('Medium', 3), ('High', 5)], onchange=set_sensitivity)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)

pygame.quit()
sys.exit()