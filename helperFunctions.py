import pygame
import numpy as np
import os
import Obstacles
from globalVars import getVars

WIDTH, HEIGHT = getVars(['width', 'height'])

def createGroundObstacle():
    image = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/stronq_doge.png').convert_alpha()
    image = pygame.transform.scale(image, (80, 150))
    obstacle = Obstacles.GroundObstacle(image)

    return obstacle