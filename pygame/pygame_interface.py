import pygame
from classes import McGyver
import os
import numpy as np

def game(win, game_display, x ,y) :

    ''' Main loop of the game :
    win : bool
    game_display : screen of the game
    x,y : int - position of McGyver

    return :
    win : bool
    x,y : updated position of mcGyver
    '''

    x_change = 0
    y_change = 0
    white = (255,255,255)
    while not win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0

        x += x_change
        y += y_change
        game_display.fill(white)
        return win, x,y


def display_mc_gyver(x, y, game_display, image_mcGyver):
    game_display.blit(image_mcGyver, (x, y))


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

def main():
    ''' Main loop of the game '''
    pygame.init()
    game_display = pygame.display.set_mode((500, 500)) #The screen of the game
    pygame.display.set_caption('The Maze 2.0')
    image_mc_gyver, get_rect = load_image('MacGyver.png')
    clock = pygame.time.Clock() #set a clock to define FPS

    ''' Setting initials variable '''

    x = 0
    y = 0
    win = False

    # Get the full path from where we execute the script
    get_dir = os.path.dirname(os.path.abspath(__file__))

    while not win :
        win,x,y = game(win, game_display, x, y) 
        display_mc_gyver(x,y, game_display, image_mc_gyver)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
