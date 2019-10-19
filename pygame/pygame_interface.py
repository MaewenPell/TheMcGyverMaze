

import os
import sys
import pygame
from pygame.locals import *
from classes import McGyver



def load_image(name, colorkey=None):
    fullname = os.path.join('ressources', name)
    
    try :
        image = pygame.image.load(fullname)
    except pygame.error as message :
        print("Cannot load image : ", name)
        raise SystemExit(message)
    
    image = image.convert() #adapt to the display
    if colorkey is not None:
        if colorkey is -1 :
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def main():
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption('The Maze')

    mcGyver = McGyver()
    allsprites = pygame.sprite.RenderPlain((mcGyver))
    clock = pygame.time.Clock()

    while 1 :
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return 
        allsprites.update()
        allsprites.draw(screen)
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
    
