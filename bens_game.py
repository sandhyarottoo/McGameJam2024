import pygame
import pygame_menu # install this using ==> pip install pygame-menu -U
import numpy as np
from globalVars import getVars
from ObjectClasses.BackgroundObject import BackgroundObject
import sys
import os

WIDTH, HEIGHT, dt , GAME_NAME = getVars(['width', 'height', 'dt', 'game_name'])

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()

### OBJECT SETUP ###

catImage = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/media/cat.png').convert_alpha()
catImage = pygame.transform.scale(catImage, (100, 100))
cat = BackgroundObject(catImage)

backgroundGroup = pygame.sprite.Group()
backgroundGroup.add(cat)

### STARTING GAME LOOP ###

def start_game():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            # elif event.type == pygame.K_ESCAPE or event.type == pygame.K_DELETE:
            #     running = False

            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         bucket.vel.x -= bucket.walkSpeed
            #     if event.key == pygame.K_RIGHT:
            #         bucket.vel.x += bucket.walkSpeed
            #     if event.key == pygame.K_SPACE:
            #         position, velocity = getInitialParams()
            #         ball.pos = position
            #         ball.vel = velocity
                    
            # elif event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT:
            #         if pygame.key.get_pressed()[pygame.K_RIGHT]:
            #             bucket.vel.x += bucket.walkSpeed
            #         else:
            #             bucket.vel.x = 0
            #     if event.key == pygame.K_RIGHT:
            #         if pygame.key.get_pressed()[pygame.K_LEFT]:
            #             bucket.vel.x -= bucket.walkSpeed
            #         else:
            #             bucket.vel.x = 0
            

        screen.fill((0,0,0))

        backgroundGroup.update(dt)
        backgroundGroup.draw(screen)


        pygame.display.flip()
        

# Setting up the menua theme
main_theme = pygame_menu.Theme(background_color=(200, 200, 150, 255),
                               title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_UNDERLINE_TITLE)

# initializing menu
menu = pygame_menu.Menu(GAME_NAME, WIDTH, HEIGHT, theme=main_theme)

menu.add.button('Play', start_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)

pygame.quit()
sys.exit()