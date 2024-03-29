import pygame
import numpy as np
import os
from ObjectClasses.BackgroundObject import BackgroundObject
import ObjectClasses.Obstacles as Obstacles
from ObjectClasses.player import PlayerHealth
from ObjectClasses.player import Player as Player
from globalVars import getVars
import ObjectClasses.enemies as enemies


WIDTH, HEIGHT, g_obs_dims = getVars(['width', 'height', 'g_obs_dims'])

def createGroundObstacle(image):
    
    obstacle = Obstacles.GroundObstacle(image)

    return obstacle

def createPlatform(image, low = True):
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
    
    model = BackgroundObject(image)
    model.vel.x = 0

    return model

def createPlayer():
    
    physicist = Player(os.path.dirname(os.path.realpath(__file__)) + '/media/physicist_v1.png')
    return physicist


def createBullet(imagepos, imageneg, xpos, ypos, mode):
    signs = [-1,1]
    num = np.random.choice(signs)
    bullet = enemies.ChargeBullet(num,imagepos,imageneg, xpos, ypos, mode)

    return bullet
#blabla

def createLife():
    image = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/Star.png').convert_alpha()
    image = pygame.transform.scale(image,(20,20))

    life1 = PlayerHealth(image,10,20)
    life2 = PlayerHealth(image,40,20)
    life3 = PlayerHealth(image,70,20)

    return life1,life2,life3


def createLaser(image, posx,posy,mode):
    image = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/Laser.png').convert_alpha()
    laser = enemies.Laser(image, posx,posy,mode)
    return laser

def createLaserWarning(radius,laser):
    laserwarning = enemies.LaserWarning(radius,laser)
    return laserwarning



