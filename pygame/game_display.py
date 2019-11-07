import game_display
import pygame
import pygame.locals
import math
import os
import configparser

def loads_tiles_tables(filename, width, height):
    path = os.getcwd() + '/pygame/' + filename
    image = pygame.image.load(path).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, math.floor(image_width / width)):
        line = []
        tile_table.append(line)
        for tile_y in range(0, math.floor(image_height / height)):
            rect = (tile_x * width, tile_y * height, width, height)
            line.append(image.subsurface(rect))
    return tile_table

def main():
    game_over = False
    while not game_over :
        screen = pygame.display.set_mode((520, 160))
        screen.fill((255, 255, 255))
        table = loads_tiles_tables('structures.png', 20, 20)
        for x, row, in enumerate(table):
            for y, tile in enumerate(row):
                screen.blit(tile, (x * 32, y * 24))
        overlays.draw(screen)
        pygame.display.flip()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                game_over = True
            elif event.type == pygame.locals.KEYDOWN:
                pressed_key = event.key

class Level(object):
    def load_file(self, filname="map.map"):
        self.map = []
        self.key = {}
        parser = configparser.ConfigParser()
        parser.read(filname)
        self.tileset = parser.get("level", "tileset")
        self.map = parser.get("level", "map").split("\n")
        for section in parser.sections():
            if len(section) == 1:
                desc = dict(parser.items(section))
                self.key[section] = desc
        self.width = len(self.map[0])
        self.height = len(self.map)

    def get_tile(self, x, y):
        try:
            char = self.map[y][x]
        except IndexError:
            return {}
        try:
            return self.key[char]
        except KeyError:
            return {}

    def get_bool(self, x, y, name):
        value = self.get_tile(x, y).get(name)
        return value in (True, 1, 'true', 'yes', 'True', 'Yes', '1', 'on', 'On')

    def is_wall(self, x, y):
        return self.get_bool(x, y, 'wall')

    def is_blocking(self, x, y):
        if not 0 <= x <= self.width or not 0 <= y <= self.height:
            return True
        return self.get_bool(x, y, 'block')

    def render(self):
        wall = self.is_wall
        tiles = MAP_CACHE[self.tileset]
        image = pygame.Surface(
            (self.width*MAP_TILE_WIDTH, self.height*MAP_TILE_HEIGHT))
        overlays = {}
        for map_y, line in enumerate(self.map):
            for map_x, c in enumerate(line):
                if wall(map_x, map_y):
                    # Draw different tiles depending on neighbourhood
                    if not wall(map_x, map_y+1):
                        if wall(map_x+1, map_y) and wall(map_x-1, map_y):
                            tile = 0, 2 #wall left and right but no wall below
                        elif wall(map_x+1, map_y):
                            tile = 0, 2
                        elif wall(map_x-1, map_y):
                            tile = 0, 2
                        else:
                            tile = 0, 2
                    else:
                        if wall(map_x+1, map_y+1) and wall(map_x-1, map_y+1):
                            tile = 0, 2
                        elif wall(map_x+1, map_y+1):
                            tile = 0, 2
                        elif wall(map_x-1, map_y+1):
                            tile = 0, 2
                        else:
                            tile = 0, 2
                    # Add overlays if the wall may be obscuring something
                    if not wall(map_x, map_y-1):
                        if wall(map_x+1, map_y) and wall(map_x-1, map_y):
                            over = 1, 0
                        elif wall(map_x+1, map_y):
                            over = 0, 0
                        elif wall(map_x-1, map_y):
                            over = 2, 0
                        else:
                            over = 3, 0
                        overlays[(map_x, map_y)] = tiles[over[0]][over[1]]
                else:
                    try:
                        tile = self.key[c]['tile'].split(',')
                        tile = int(tile[0]), int(tile[1])
                    except (ValueError, KeyError):
                        # Default to ground tile
                        tile = 0, 3
                tile_image = tiles[tile[0]][tile[1]]
                image.blit(tile_image,
                           (map_x*MAP_TILE_WIDTH, map_y*MAP_TILE_HEIGHT))
        return image, overlays


if __name__ == '__main__' :
    pygame.init()
    screen = pygame.display.set_mode((424, 320))

    MAP_TILE_WIDTH = 15
    MAP_TILE_HEIGHT = 15
    MAP_CACHE = {
        'structures.png' : loads_tiles_tables('structures.png', MAP_TILE_WIDTH, MAP_TILE_HEIGHT),
    }

    level = Level()
    path = os.getcwd() + '/pygame/' + 'map.map' 
    level.load_file(path)

    clock = pygame.time.Clock()

    background, overlay_dict = level.render()
    overlays = pygame.sprite.RenderUpdates()
    for (x,y), image in overlay_dict.items():
        overlay = pygame.sprite.Sprite(overlays)
        overlay.image = image
        overlay.rect = image.get_rect().move(x * 24, y * 16 - 16)
    screen.blit(background, (0,0))
    overlays.draw(screen)
    pygame.display.flip()
    main()
    
