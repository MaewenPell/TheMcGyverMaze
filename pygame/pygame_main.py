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
        ''' Initialize game data'''
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100) #key pressed > 500ms we repeat this key every 100ms
        self.load_data()

    def load_data(self):
        ''' Definition of the images and the map '''

        game_folder = path.dirname(__file__)
        image_folder = path.join(game_folder, 'ressource')
        map_folder = path.join(game_folder, 'maps')

        self.map = TiledMap(path.join(map_folder, 'map_1.tmx')) #We load the map we created with Tiled 

        self.map_img = self.map.make_map() #We define a Surface of width * height to countain the map
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(image_folder, PLAYER_IMG)).convert_alpha()
        self.boss_img = pg.image.load(path.join(image_folder, BOSS_IMG)).convert_alpha()
        self.item_images = {}
        for item in ITEMS_IMAGES : #We load and assign images in a dict : {'game_name' : 'images_name.png'}
            self.item_images[item] = pg.image.load(path.join(image_folder, ITEMS_IMAGES[item])).convert_alpha()

        #self.map = Map(path.join(game_folder, 'map2.txt')) #Old map

    def new(self):
        ''' Scanning the tmx map and assign elems to Classes'''
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.items = pg.sprite.Group()

        object_possible_location = []

        ''' Read all the tiles and if it's particular ones assign them to the related classes 
        '''
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

        ''' Object managing : 
        1- We generate a random index between 0 and the number of possible location
        2- For each item we create an instance of Item and place it in the maze at the place defined randomly
        3- We delete this location so we can't have two items at the same location
        '''
        index = randint(0, len(object_possible_location) - 1)
        self.items1 = Item(self, object_possible_location[index][0], object_possible_location[index][1], 'tube')
        object_possible_location.pop(index)

        index = randint(0, len(object_possible_location) - 1)
        self.items2 = Item(self, object_possible_location[index][0], object_possible_location[index][1], 'ether')
        object_possible_location.pop(index)

        index = randint(0, len(object_possible_location) - 1)
        self.items3 = Item(self, object_possible_location[index][0], object_possible_location[index][1], 'seringue')
        object_possible_location.pop(index)

        #     OLD way to load map
        # for row,tiles in enumerate(self.map.data):
        #     for col, tile in enumerate(tiles):
        #         if tile == 'O':
        #             Wall(self,col, row)
        #         if tile == '&':
        #             self.player = Player(self, col, row)

    def run(self):
        ''' Main loop of the game '''
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000 #We make this to move at constant speed not base on the framerate
            self.events() #If the player click on quit or want to leave the game
            self.update() #Catching all the changes that happen during one loop 
            self.draw()

    def quit(self):
        ''' Quit the game ''' 
        pg.quit()
        sys.exit()

    def update(self):
        ''' Catching all the actions '''
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.items, True) #If the player walk on an item we delete it from the maze and add it in the collected item
        for hit in hits : 
            self.player.invetory.append(hit)

        if pg.sprite.collide_rect(self.player, self.boss) : #If we collide with the boss we check if we have all the three items, and so we kill the boss else we loose
            if len(self.player.invetory) == 3 :
                self.boss.kill() #TODO : write a message on the screen and make a quit statement
            else :
                self.quit() #TODO : write a message on the screen to say we loose

    # def draw_grid(self):
    #     for x in range(0, WIDTH, TILESIZE):
    #         pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
    #     for y in range(0, HEIGHT, TILESIZE):
    #         pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        ''' Drawn item on the screen '''
        #self.screen.fill(BGCOLOR)
        #self.draw_grid()
        self.screen.blit(self.map_img, self.map_rect)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        ''' Catching the events during the game '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

if __name__ == "__main__" :
    g = Game()
    while True:
        g.new()
        g.run()
