import pygame as pg


class Boss(pg.sprite.Sprite):
    ''' The class who's handle the boss '''

    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.boss_img
        self.rect = pg.Rect(x, y, w, h)
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
