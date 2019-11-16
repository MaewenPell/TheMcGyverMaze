import os
import sys
import const as cs
from random import randint
from items import Object
from mc_gyver import McGyver


class Motor(Object, McGyver):
    '''Class who will handle the execution of the game '''
    def __init__(self):
        '''We load the file containing the map'''
        get_dir = get_dir = os.path.dirname(os.path.abspath(__file__))
        with open(get_dir + '/map.txt') as fichier:
            txt_map = fichier.read()

        ''' We call the differents method of the class '''

        self.maze = self.coords_generator(txt_map)
        self.needle_object = Object(cs.NEEDLE)
        self.tube_object = Object(cs.TUBE)
        self.ether_object = Object(cs.ETHER)
        self.mc_gyver = McGyver()
        self.wall = cs.WALL
        self.enter = cs.ENTER
        self.end = cs.END
        self.mc_gyver = cs.MC_GYVER
        self.backslash = cs.BACKSLASH
        self.floor = cs.FLOOR
        self.needle = cs.NEEDLE
        self.tube = cs.TUBE
        self.ether = cs.ETHER
        self.labyrinthe_characteristics(self.maze)
        self.turn = 0
        '''We launch game loop '''
        self.game_loop()

    def labyrinthe_characteristics(self, labyrinthe_map):
        '''
        We determine wall, enter,
        exit_door, player, current_map(txt file) and position
        '''
        self.labyrinthe_map = labyrinthe_map
        self.mc_g_pos = self.get_position(self.labyrinthe_map,
                                          self.mc_gyver)
        self.end_position = self.get_position(self.labyrinthe_map, self.end)
        self.ether_position = self.get_position(self.labyrinthe_map,
                                                self.ether)
        self.needle_position = self.get_position(self.labyrinthe_map,
                                                 self.needle)
        self.tube_position = self.get_position(self.labyrinthe_map, self.tube)

    def place_objects(self):
        ''' We place the items when we find a possible spot'''
        for elem in self.needle, self.tube, self.ether:
            position_x = randint(0, 15)
            position_y = randint(0, 15)
            while self.maze[position_x, position_y] is not self.floor:
                position_x = randint(0, 15)
                position_y = randint(0, 15)
            self.maze[position_x, position_y] = elem

    def get_position(self, labyrinthe_map, elem):
        ''' We get the position of McGyvers (x,y) '''
        values = labyrinthe_map.items()
        for keys, value in values:
            if elem == value:
                return keys

    def coords_generator(self, txt_map):
        '''We assign each maze item to a (x,y) coords '''
        x = 0
        y = 0
        coord_labyrinthe_map = {}
        for elem in txt_map:
            if elem != '\n':
                coord_labyrinthe_map[(x, y)] = elem
                x += 1
            else:
                coord_labyrinthe_map[(x, y)] = elem
                x = 0
                y += 1
        return coord_labyrinthe_map

    def is_crossable_or_picked(self, element):
        ''' Return true or false depending of the element '''
        elem_crossables = [self.end, self.floor,
                           self.needle, self.tube, self.ether]
        if element in elem_crossables:
            if element is self.ether:
                self.ether_object.ispicked = True
                self.maze[self.get_position(self.maze, element)] = self.floor
            elif element is self.tube:
                self.tube_object.ispicked = True
                self.maze[self.get_position(self.maze, element)] = self.floor
            elif element is self.needle:
                self.needle_object.ispicked = True
                self.maze[self.get_position(self.maze, element)] = self.floor
            return True
        else:
            return False

    def display_maze(self, labyrinthe_map):
        if self.mc_g_pos != (0, 1):
            labyrinthe_map[0, 1] = self.enter
        if self.needle_object.ispicked:
            labyrinthe_map[self.needle_position] = self.floor
        if self.ether_object.ispicked:
            labyrinthe_map[self.ether_position] = self.floor
        if self.tube_object.ispicked:
            labyrinthe_map[self.tube_position] = self.floor
        print(''.join(labyrinthe_map.values()))

    def next_move(self, mc_g_pos, maze):
        ''' We determine if the next move is possible or not '''

        ''' We get the x,y coordinate of McGyver '''
        x_coords = mc_g_pos[0]
        y_coords = mc_g_pos[1]

        ''' We calculate the next coords depending of the move'''
        MOVE_N = x_coords, y_coords - 1
        MOVE_S = x_coords, y_coords + 1
        MOVE_E = x_coords + 1, y_coords
        MOVE_O = x_coords - 1, y_coords

        user_move = input("Entrez votre next move currently (n/s/e/o) -q : ")

        if (user_move == "q"):  # If the user want to quit the game
            sys.exit(0)
        if (user_move == "n"):
            try:  # We check if the input is not out of the bound of the dict
                if self.is_crossable_or_picked(maze[MOVE_N]):
                    self.maze[MOVE_N],
                    self.maze[self.mc_g_pos] = self.maze[self.mc_g_pos],
                    self.maze[MOVE_N]
                    self.mc_g_pos = MOVE_N  # We assign the new position
                else:
                    print("Sorry this move is impossible")
            except KeyError:
                print("Sorry this move is impossible you get out of the maze")
                user_move = input(
                    "Entrez votre next move currently (n/s/e/o) -q : ")
        elif (user_move == "s"):
            try:
                if self.is_crossable_or_picked(self.maze[MOVE_S]):
                    self.maze[MOVE_S],
                    self.maze[self.mc_g_pos] = self.maze[self.mc_g_pos],
                    self.maze[MOVE_S]
                    self.mc_g_pos = MOVE_S
                else:
                    print("Sorry this move is impossible")
            except KeyError:
                print("Sorry this move is impossible you get out of the maze")
                user_move = input(
                    "Entrez votre next move currently (n/s/e/o) -q : ")
        elif (user_move == "e"):
            try:
                if self.is_crossable_or_picked(self.maze[MOVE_E]):
                    self.maze[MOVE_E],
                    self.maze[self.mc_g_pos] = self.maze[self.mc_g_pos],
                    self.maze[MOVE_E]
                    self.mc_g_pos = MOVE_E
                else:
                    print("Sorry this move is impossible")
            except KeyError:
                print("Sorry this move is impossible you get out of the maze")
                user_move = input(
                    "Entrez votre next move currently (n/s/e/o) -q : ")
        elif (user_move == "o"):
            try:
                if self.is_crossable_or_picked(self.maze[MOVE_O]):
                    self.maze[MOVE_O],
                    self.maze[self.mc_g_pos] = self.maze[self.mc_g_pos],
                    self.maze[MOVE_O]
                    self.mc_g_pos = MOVE_O
                else:
                    print("Sorry this move is impossible")
            except KeyError:
                print("Sorry this move is impossible you get out of the maze")
                user_move = input(
                    "Entrez votre next move currently (n/s/e/o) -q : ")
        else:
            print(
                "Wrong you didn't enter a correct direction")

    def game_loop(self):
        ''' The main loop of the game'''
        self.place_objects()
        while(self.mc_g_pos != self.end_position):
            self.display_maze(self.maze)
            self.next_move(self.mc_g_pos, self.maze)

        if self.ether_object.ispicked \
            and self.tube_object.ispicked and \
                self.needle_object.ispicked:
            print("---- Congratulation you win the game ----")
        else:
            print("---- Sorry, You loose ---")


if __name__ == "__main__":
    test = Motor()
