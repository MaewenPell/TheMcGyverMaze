import pygame as pg


class Item(pg.sprite.Sprite):
    ''' Class who handle all the items we can pick inside the maze '''
    def __init__(self, game, x, y, type):
        self.groups = game.all_sprites, game.items
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.item_images[type]
        self.rect = self.image.get_rect()
        self.type = type
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
