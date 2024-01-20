import pygame
import numpy as np
import os
import ObjectClasses.BackgroundObject as BackgroundObject
import ObjectClasses.Obstacles as Obstacles
from globalVars import getVars

WIDTH, HEIGHT, g_obs_dims = getVars(['width', 'height', 'g_obs_dims'])

pygame.mixer.init()
jump_grunt = pygame.mixer.Sound(os.path.realpath(__file__) + "media/Audio/Grunt 1.wav")

def jumpSound():
    pygame.mixer.Sound.play(jump_grunt)