import pygame
import numpy as np
import os
import ObjectClasses.BackgroundObject as BackgroundObject
import ObjectClasses.Obstacles as Obstacles
from globalVars import getVars

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
        image = pygame.transform.scale(image, (200, 200))
    
    model = BackgroundObject(image)
    model.vel.x = 0

    return model