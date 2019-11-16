import sys
from os import path
from random import randint

import pygame as pg

import settings as st
import sprites as sprt
import tilemap as tlm


class Game:
    def __init__(self):
        ''' Initialize game data'''
        pg.init()
        self.screen = pg.display.set_mode((st.WIDTH, st.HEIGHT))
        pg.display.set_caption(st.TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)  # key pressed > 500ms repeat every 100ms
        self.load_data()

    def load_data(self):
        ''' Definition of the images and the map '''

        self.game_folder = path.dirname(__file__)
        self.image_folder = path.join(sprt.game_folder, 'ressource')
        self.map_folder = path.join(sprt.game_folder, 'maps')
        self.font = path.join(sprt.image_folder, 'game_over.ttf')
        self.player_img = pg.image.load(
            path.join(sprt.image_folder, st.PLAYER_IMG)).convert_alpha()
        self.end_img = pg.image.load(
            path.join(sprt.image_folder, st.END_IMG)).convert_alpha()
        self.boss_img = pg.image.load(
            path.join(sprt.image_folder, st.BOSS_IMG)).convert_alpha()
        self.item_images = {}
        for item in st.ITEMS_IMAGES:
            # We load and assign images {'game_name' : 'images_name.png'}
            self.item_images[item] = pg.image.load(
                path.join(sprt.image_folder,
                          st.ITEMS_IMAGES[item])).convert_alpha()

    def new(self):
        ''' Scanning the tmx map and assign elems to Classes'''
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.items = pg.sprite.Group()
        # We load the map we created with Tiled
        self.map = tlm.TiledMap(path.join(self.map_folder, st.MAP))
        # We define a Surface of width * height to countain the map
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.obj_poss_loc = []
        self.end_game = False
        self.end_game_win = False

        ''' Read all the tiles :
            and assign them to the related class
        '''
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                self.player = sprt.Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                self.wall = sprt.Obstacle(self, tile_object.x,
                                          tile_object.y, tile_object.width,
                                          tile_object.height)
            if tile_object.name == 'boss':
                self.boss = sprt.Boss(self, tile_object.x,
                                      tile_object.y, tile_object.width,
                                      tile_object.height)
            if tile_object.name == 'end':
                self.end = sprt.End(self, tile_object.x,
                                    tile_object.y, tile_object.width,
                                    tile_object.height)
            if tile_object.name == 'object':
                self.obj_poss_loc.append(
                    (tile_object.x, tile_object.y))

        self.place_objects('tube')
        self.place_objects('ether')
        self.place_objects('seringue')

    def place_objects(self, type):
        '''
        Object managing :
        1- We generate a random index between 0 and the len of possible loc
        2- For each item we create an instance of Item
           and place it in the maze at the place defined randomly
        3- We delete this location so we can't have two items at the same place
        '''

        index = randint(0, len(self.obj_poss_loc) - 1)
        sprt.Item(self, self.obj_poss_loc[index][0],
                  self.obj_poss_loc[index][1],
                  type)

    def run(self):
        ''' Main loop of the game '''
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(st.FPS) / 1000
            # move at constant speed not base on the framerate
            self.events()
            self.update()  # Catching all the changes that happen during a loop
            self.draw()

    def quit(self):
        ''' Quit the game '''
        pg.quit()
        sys.exit()

    def update(self):
        ''' Catching all the actions '''
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.items, True)
        # If the player walk on an item we delete it
        # from the maze and add it in the collected item
        for hit in hits:
            self.player.inventory.append(hit.type)
        if pg.sprite.collide_rect(self.player, self.boss):
            # If we collide with the boss :
            # we check if we have all the three items
            # if so we kill the boss else we loose
            if len(self.player.inventory) == 3:
                self.boss.kill()
            else:
                self.end_game = True
                self.end_game_win = False
                self.playing = False
        if pg.sprite.collide_rect(self.player, self.end):
            if len(self.player.inventory) == 3:
                self.end_game = True
                self.end_game_win = True
                self.playing = False

    def draw(self):
        ''' Drawn item on the screen '''
        self.screen.blit(self.map_img, self.map_rect)
        self.all_sprites.draw(self.screen)
        self.draw_text("Items picked : {}".format(
                       len(self.player.inventory)),
                       pg.font.get_default_font(),
                       20, st.GREEN, st.WIDTH/2, 20,
                       align='center')
        pg.display.flip()

    def events(self):
        ''' Catching the events during the game '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def draw_text(self, text, font_name, size, color, x, y, align='nw'):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == 'center':
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def show_game_over_screen(self):
        self.screen.fill(st.BLACK)
        if self.end_game_win is True:
            self.draw_text("Congratulation ! You win", self.font,
                           50, st.GREEN, st.WIDTH / 2,
                           st.HEIGHT / 2, align='center')
        else:
            self.draw_text("GAME OVER ! You loose", self.font, 50,
                           st.RED, st.WIDTH / 2, st.HEIGHT / 2, align='center')
        self.draw_text("Press 'r' to restart or 'q' to quit",
                       pg.font.get_default_font(), 15,
                       st.WHITE, st.WIDTH / 2, st.HEIGHT * 3/4, align='center')
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        pg.event.wait()
        waiting = True
        while waiting is True:
            self.clock.tick(st.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        waiting = False
                    elif event.key == pg.K_q:
                        self.quit()


if __name__ == "__main__":
    g = Game()
    while True:
        g.new()
        g.run()
        g.show_game_over_screen()
