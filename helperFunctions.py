import pygame
import numpy as np
import os
from ObjectClasses.BackgroundObject import BackgroundObject
import ObjectClasses.Obstacles as Obstacles
from ObjectClasses.player import Player as Player
from globalVars import getVars
import ObjectClasses.enemies as enemies


WIDTH, HEIGHT, g_obs_dims = getVars(['width', 'height', 'g_obs_dims'])

def createGroundObstacle():
    image = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/stronq_doge.png').convert_alpha()
    image = pygame.transform.scale(image, g_obs_dims)
    obstacle = Obstacles.GroundObstacle(image)

    return obstacle

def createPlatform(low = True):
    image = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/lebron.jpeg').convert_alpha()
    image = pygame.transform.scale(image, (80, 20))

    if low:
        platform = Obstacles.Platform(image, np.random.randint(HEIGHT - g_obs_dims[1] - 50, HEIGHT - g_obs_dims[1]))
    else:
        platform = Obstacles.Platform(image, np.random.randint(HEIGHT - g_obs_dims[1] - 300, HEIGHT - g_obs_dims[1] - 100))

    return platform

def createMotionCaptureModel(string):
    image = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/garfgarf.png').convert_alpha()

    if string == 'player':
        image = pygame.transform.scale(image, (80, 100))

    elif string == 'contraption':
        image = pygame.transform.scale(image, (100, 300))
    
    model = BackgroundObject(image, 20, pygame.Vector2(20, 20))
    model.vel.x = 0

    return model

def createPlayer():
    
    physicist = Player(os.path.dirname(os.path.realpath(__file__)) + '/media/physicist_v1.png')
    return physicist


def createBullet():

    imageneg = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/Soccer_Ball.png').convert_alpha()
    imagepos = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/Basketball_PNG.png').convert_alpha()

    imageneg = pygame.transform.scale(imageneg, (100, 100))
    imagepos = pygame.transform.scale(imagepos, (100, 100))

    signs = [-1,1]
    num = np.random.choice(signs)
    bullet = enemies.ChargeBullet(num,imagepos,imageneg)

    return bullet


