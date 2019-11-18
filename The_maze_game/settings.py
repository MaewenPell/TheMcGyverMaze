''' Define some usefull colors '''

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

''' Game settings '''

MAP = 'map_1.tmx'
WIDTH = 300  # 20 px tiles * 15 tiles
HEIGHT = 320
FPS = 60
TITLE = "The McGyver Maze"

TILESIZE = 20
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

'''Player settings '''

PLAYER_SPEED = 150
PLAYER_IMG = 'MacGyver.png'
BOSS_IMG = 'Gardien.png'
END_IMG = 'end_img.png'


''' ITEMS PROPERTIES '''

ITEMS_IMAGES = {'needle': 'seringue.png',
                'tube': 'tube_plastique.png', 'ether': 'ether.png'}
