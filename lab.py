class Maze:
    def __init__(self, wall, enter, exit_door, player, current_map):
        self.wall = wall
        self.enter = enter
        self.exit_door = exit_door
        self.player = player
        self.current_map = current_map
        self.current_position = current_map.find(player)
        self.iswin = current_map.find(exit_door)

    def is_crossable(self, element):
        ''' Return true or false depending of the element founded '''
        if element == self.wall:
            return False
        elif element == self.enter:
            return True
        elif element == self.exit_door:
            return True
        else:
            return True
