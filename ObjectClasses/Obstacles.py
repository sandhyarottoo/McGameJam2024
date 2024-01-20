import pygame
from globalVars import getVars

WIDTH, HEIGHT, speed = getVars(['width', 'height', 'obstacle_speed'])

class GroundObstacle(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()

        self.pos = pygame.Vector2(WIDTH + image.get_width()/2, HEIGHT - 10 - image.get_height()/2)
        self.vel = pygame.Vector2(speed, 0)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x, self.pos.y)
    
    def update(self, dt):
        # make it disappear when it passes the screen 
        if self.pos.x + self.image.get_width()/2 < 0:
            self.kill()
        else:
            self.pos += self.vel*dt
            self.rect.center = (self.pos.x, self.pos.y)


class Platform(pygame.sprite.Sprite):
    def __init__(self, image, ypos):
        super().__init__()

        self.pos = pygame.Vector2(WIDTH + image.get_width()/2, ypos)
        self.vel = pygame.Vector2(speed, 0)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x, self.pos.y)
    
    def update(self, dt):
        # make it disappear when it passes the screen 
        if self.pos.x + self.image.get_width()/2 < 0:
            self.kill()
        else:
            self.pos += self.vel*dt
            self.rect.center = (self.pos.x, self.pos.y)

