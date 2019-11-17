import os

import pygame as pg

import settings as st

game_folder = os.path.dirname(__file__)
image_folder = os.path.join(game_folder, 'ressource')


class Player(pg.sprite.Sprite):
    ''' Class who handle McGyver and his moves through the maze'''
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.player_img
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x
        self.y = y
        self.inventory = []

    def get_keys(self):
        ''' Handle the keys moves '''
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_q]:
            self.vx = - st.PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = st.PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_z]:
            self.vy = - st.PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = st.PLAYER_SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
            # For the diagonal moves we need
            # to multiply by 1sqrt2 depends on pythagore theorem,
            # otherwise we  would walk faster

    def collide_with_walls(self, dir):
        '''
        We check in the list of walls,
        if will walk on an existing (x,y) wall location
        '''
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                    # We minus the width because we consider rect.left side
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
            elif self.x < 0:
                self.vx = 0
                self.rect.x = 0
            elif self.x >= st.WIDTH - self.rect.width:
                self.vx = 0
                self.x = st.WIDTH - self.rect.width
                self.rect.x = self.x

        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
            elif self.y < 0:
                self.vy = 0
                self.rect.y = 0
            elif self.y >= st.HEIGHT - self.rect.width:
                self.vy = 0
                self.y = st.HEIGHT - self.rect.width
                self.rect.y = self.y

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')


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


class Obstacle(pg.sprite.Sprite):
    ''' The class who handle all the walls '''
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y


class End(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.end_img
        self.rect = pg.Rect(x, y, w, h)
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y