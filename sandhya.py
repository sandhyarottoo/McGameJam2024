
import numpy as np
import pygame
import sys
import os
from globalVars import getVars
from BackgroundObject import BackgroundObject

path = os.getcwd() + '/media/cat.png'
print(path)

WIDTH, HEIGHT, dt, PLAYERXVEL,PLAYERYVEL = getVars(['width', 'height', 'dt','playerVelocity','jumpVel'])



# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

### OBJECT SETUP ###


WIDTH = 1200
HEIGHT = 800

class Player(pygame.sprite.Sprite):
    def __init__(self,image,):
        super().__init__()
        self.image = pygame.image.load(image)
        self.yvelocity = PLAYERYVEL
        self.xvelocity = PLAYERXVEL
        self.rect = self.image.get_rect()


    def update(self,keys):
        
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.xvelocity*dt
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.xvelocity*dt
        if keys[pygame.K_UP]:
            self.rect.y -= self.yvelocity*dt
        if keys[pygame.K_DOWN]:
            self.rect.y += self.yvelocity*dt
      

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player(path)
players = pygame.sprite.Group()
players.add(player)

def run_game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                

        # Clears the screen
        screen.fill((50, 50, 60))
        screen.blit(player.image,player.rect)
        keys = pygame.key.get_pressed()

        player.update(keys)
        players.draw(screen)
        pygame.display.flip()
        clock.tick(60)


run_game()