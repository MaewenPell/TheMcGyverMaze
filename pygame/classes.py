import pygame
import os
import sys
from pygame.locals import *



class McGyver(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def _walk(self, x, y):
        newpos = self.rect.move((x,y))
        self.rect = newpos
    