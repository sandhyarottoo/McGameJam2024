import pygame
import numpy as np
import os
import ObjectClasses.BackgroundObject as BackgroundObject
import ObjectClasses.Obstacles as Obstacles
from globalVars import getVars

WIDTH, HEIGHT, g_obs_dims = getVars(['width', 'height', 'g_obs_dims'])

pygame.init()
pygame.mixer.init()

def playJump():
    sound_file_path = os.path.dirname(os.path.realpath(__file__)) + "/media/Audio/Grunt 1.wav"
    pygame.mixer.music.load(sound_file_path)
    pygame.mixer.music.play()

def playMusic():
    sound_file_path = os.path.dirname(os.path.realpath(__file__)) + "/media/Audio/Music.wav"
    pygame.mixer.music.load(sound_file_path)
    pygame.mixer.music.play(loops=-1)