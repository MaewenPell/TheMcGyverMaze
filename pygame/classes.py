import pygame
import os
import sys
from pygame.locals import *

def load_image(name, colorkey=None):
    fullname = os.path.join(os.getcwd(), 'ressource', name)
    print(fullname)

    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print("Cannot load image : ", name)
        raise SystemExit(message)

    image = image.convert()  # adapt to the display
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class McGyver(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('MacGyver.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10,10
        self.move = 9

    def _update(self):
        self._walk()

    def _walk(self):
        newpos = self.rect.move((self.move))
        if not self.area.countains(newpos):
            if self.rect.left < self.area.left or self.react.right > self.area.right :
                self.move = -self.move
                newpos = self.rect.move((self.move, 0))
                self.image = pygame.transform.flip(self.image, 1, 0)
            self.rect = newpos
    