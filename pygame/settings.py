''' Define some usefull colors '''

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

''' Game settings '''

WIDTH = 300  # 20 px tiles * 15 tiles
HEIGHT = 300  
FPS = 60
TITLE = "The McGyver Maze"
BGCOLOR = DARKGREY

TILESIZE = 20
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

'''Player settings '''

PLAYER_SPEED = 150
PLAYER_IMG = 'MacGyver.png'
BOSS_IMG = 'Gardien.png'



''' ITEMS PROPERTIES '''

ITEMS_IMAGES = {'seringue' : 'seringue.png', 'tube' : 'tube_plastique.png', 'ether' : 'ether.png' }