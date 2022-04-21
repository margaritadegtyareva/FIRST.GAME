import pygame

class Object:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.image=pygame.transform.scale(pygame.image.load("img.png"),(100,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
