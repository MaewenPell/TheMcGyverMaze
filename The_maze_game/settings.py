''' Define some usefull colors used to display message on the screen'''

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

''' Game settings '''

MAP = 'map_1.tmx'  # this constante is used if you want to load another map
WIDTH = 300  # Absolute size of the map : 20 px per tiles * 15 tiles
HEIGHT = 320  # Same but + 20 for another tile at the end to display items
FPS = 60
TITLE = "The McGyver Maze"

TILESIZE = 20  # This is the pixel size of one tile
GRIDWIDTH = WIDTH / TILESIZE  # Size in tile
GRIDHEIGHT = HEIGHT / TILESIZE

'''Player settings '''

PLAYER_SPEED = 150  # How fast the player will move across the maze (px / move)
PLAYER_IMG = 'MacGyver.png'
BOSS_IMG = 'Gardien.png'
END_IMG = 'end_img.png'


''' ITEMS PROPERTIES '''

ITEMS_IMAGES = {'needle': 'seringue.png',
                'tube': 'tube_plastique.png', 'ether': 'ether.png'}
