import pygame as pg
import sys
from settings import *
from sprites import *
from os import path
from tilemap import *
from random import randint
import pytmx


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        image_folder = path.join(game_folder, 'ressource')
        map_folder = path.join(game_folder, 'maps')
        #self.map = Map(path.join(game_folder, 'map2.txt')) #Old map
        self.map = TiledMap(path.join(map_folder, 'map_1.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(image_folder, PLAYER_IMG)).convert_alpha()
        self.boss_img = pg.image.load(path.join(image_folder, BOSS_IMG)).convert_alpha()
        self.item_images = {}
        for item in ITEMS_IMAGES :
            self.item_images[item] = pg.image.load(path.join(image_folder, ITEMS_IMAGES[item])).convert_alpha()

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.items = pg.sprite.Group()
        #     OLD way to load map
        # for row,tiles in enumerate(self.map.data):
        #     for col, tile in enumerate(tiles):
        #         if tile == 'O':
        #             Wall(self,col, row)
        #         if tile == '&':
        #             self.player = Player(self, col, row)
        object_possible_location = []
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                self.wall = Obstacle(self, tile_object.x,
                                     tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'boss':
                self.boss = Boss(self, tile_object.x,
                                 tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'object':
                object_possible_location.append((tile_object.x, tile_object.y))
    
        ''' Object managing '''
        index = randint(0, len(object_possible_location) - 1)
        self.items1 = Item(self, object_possible_location[index][0], object_possible_location[index][1], 'tube')
        object_possible_location.pop(index)
        index = randint(0, len(object_possible_location) - 1)

        self.items2 = Item(self, object_possible_location[index][0], object_possible_location[index][1], 'ether')
        object_possible_location.pop(index)
        index = randint(0, len(object_possible_location) - 1)

        self.items3 = Item(
            self, object_possible_location[index][0], object_possible_location[index][1], 'seringue')
        object_possible_location.pop(index)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000 #We make this to move at constant speed not base on the framerate
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        # player walk on a item 
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.items, True)
        for hit in hits :
            self.player.invetory.append(hit)
        
        hits_boss = pg.sprite.collide_rect(self.player, self.boss)
        if len(self.player.invetory) == 3 :
            hits_boss.kill()
        #else :
            #self.quit()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        #self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.screen.blit(self.map_img, self.map_rect)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
