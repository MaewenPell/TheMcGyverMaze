import os
import sys
from const import WALL, MC_GYVER, START, END, FLOOR, WIDTH, ENTER, BACKSLASH, TUBE, NEEDLE, ETHER
from random import randint
from items import Object

#TODO : Patch swap elem when they need to be display or not

class Motor(Object):
    '''Class who will handle the execution of the game '''
    def __init__(self):
        '''We load the file countaining the map'''
        get_dir = get_dir = os.path.dirname(os.path.abspath(__file__))
        with open(get_dir + '/map.txt') as fichier:
            txt_map = fichier.read()

        ''' We call the differents method of the class '''
        self.maze = self.coords_generator(txt_map) #we create à dict object from txt map
        self.needle_object = Object(NEEDLE)
        self.tube_object = Object(TUBE)
        self.ether_object = Object(ETHER)
        self.labyrinthe_characteristics(WALL, ENTER, END, MC_GYVER, BACKSLASH, FLOOR, self.needle_object.repr(NEEDLE), self.tube_object.repr(TUBE), self.ether_object.repr(ETHER), self.maze) #We determines elements of the maze
        '''We launch game loop '''
        self.game_loop()
        

    def labyrinthe_characteristics(self, WALL, ENTER, END, MC_GYVER, BACKSLASH, FLOOR, NEEDLE, TUBE, ETHER, labyrinthe_map):
        ''' We determine wall, enter, exit_door, player, current_map(txt file) and position'''
        self.wall = WALL
        self.enter = ENTER
        self.end = END
        self.mc_gyver = MC_GYVER
        self.backslash = BACKSLASH 
        self.floor = FLOOR
        self.needle = NEEDLE
        self.tube = TUBE
        self.ether = ETHER
        self.labyrinthe_map = labyrinthe_map
        self.mc_gyver_pos = self.get_position(self.labyrinthe_map, self.mc_gyver)
        self.end_position = self.get_position(self.labyrinthe_map, self.end)

    def place_objects(self):
        ''' We place the items when we find a possible spot'''
        for elem in self.needle, self.tube, self.ether : 
            position_x = randint(0, 15)
            position_y = randint(0, 15)
            while self.maze[position_x, position_y] is not self.floor:
                position_x = randint(0, 15)
                position_y = randint(0, 15)
            self.maze[position_x, position_y] = elem

    def get_position(self, labyrinthe_map, elem):
        ''' We get the position of McGyvers (x,y) '''
        values = labyrinthe_map.items()
        for keys, value in values : 
            if elem == value:
                return keys

    def coords_generator(self, txt_map):
        '''We assign each maze item to a (x,y) coords '''
        x = 0
        y = 0
        coord_labyrinthe_map = {}
        for elem in txt_map:
            if elem is not '\n':
                coord_labyrinthe_map[(x, y)] = elem
                x += 1
            else :
                coord_labyrinthe_map[(x, y)] = elem
                x = 0
                y += 1
        return coord_labyrinthe_map

    def is_crossable_or_picked(self, element):
        ''' Return true or false depending of the element '''
        elem_crossables = [self.enter, self.end, self.floor, self.needle, self.tube, self.ether]
        if element in elem_crossables :
            if element is self.ether : 
                self.ether_object.status(True)
            elif element is self.tube:
                self.tube_object.status(True)
            elif element is self.needle:
                self.needle_object.status(True)
            return True
        else :
            return False

    def display_maze(self, labyrinthe_map):
        print(''.join(labyrinthe_map.values()))

    def next_move(self):
        ''' We determine if the next move is possible or not '''

        ''' We get the x,y coordinate of McGyver ''' 
        x_coords = self.mc_gyver_pos[0]
        y_coords = self.mc_gyver_pos[1]

        ''' We calculate the next coords depending of the move'''
        MOVE_N = x_coords, y_coords - 1
        MOVE_S = x_coords, y_coords + 1
        MOVE_E = x_coords + 1, y_coords
        MOVE_O = x_coords - 1, y_coords

        user_move = input("Entrez votre next move currently (n/s/e/o) -q : ")
    
        if (user_move == "q"): #If the user want to quit the game
            sys.exit(0)
        if (user_move == "n"):
            try : #We check if the input is not out of the bound of the dict
                if self.is_crossable_or_picked(self.maze[MOVE_N]):
                        self.maze[MOVE_N], self.maze[self.mc_gyver_pos] = self.maze[self.mc_gyver_pos], self.maze[MOVE_N] #We swap the elems
                        self.mc_gyver_pos = MOVE_N  #We assign the new position 
                else :
                    print("Sorry this move is impossible")
            except KeyError:
                print("Sorry this move is impossible you get out of the maze")
                user_move = input("Entrez votre next move currently (n/s/e/o) -q : ")
        elif (user_move == "s"):
            try :
                if self.is_crossable_or_picked(self.maze[MOVE_S]):
                    self.maze[MOVE_S], self.maze[self.mc_gyver_pos] = self.maze[self.mc_gyver_pos], self.maze[MOVE_S]
                    self.mc_gyver_pos = MOVE_S
                else:
                    print("Sorry this move is impossible")
            except KeyError :
                print("Sorry this move is impossible you get out of the maze")
                user_move = input("Entrez votre next move currently (n/s/e/o) -q : ")
        elif (user_move == "e"):
            try :
                if self.is_crossable_or_picked(self.maze[MOVE_E]):
                    self.maze[MOVE_E], self.maze[self.mc_gyver_pos] = self.maze[self.mc_gyver_pos], self.maze[MOVE_E]
                    self.mc_gyver_pos = MOVE_E
                else:
                    print("Sorry this move is impossible")
            except KeyError:
                print("Sorry this move is impossible you get out of the maze")
                user_move = input("Entrez votre next move currently (n/s/e/o) -q : ")
        elif (user_move == "o"):
            try : 
                if self.is_crossable_or_picked(self.maze[MOVE_O]):
                    self.maze[MOVE_O], self.maze[self.mc_gyver_pos] = self.maze[self.mc_gyver_pos], self.maze[MOVE_O]
                    self.mc_gyver_pos = MOVE_O
                else:
                    print("Sorry this move is impossible")
            except KeyError: 
                print("Sorry this move is impossible you get out of the maze")
                user_move = input("Entrez votre next move currently (n/s/e/o) -q : ")
        else :
            print("Wrong you didn't enter a correct direction please enter (n/s/e/o) or (q) to quit")

    def game_loop(self):
        ''' The main loop of the game'''
        self.place_objects() #We load and place the three elems
        while(self.mc_gyver_pos != self.end_position): #While we don't have reach the end
            self.display_maze(self.maze) 
            self.next_move() 
        
        ''' We have reach the end we check if we have the three items required '''
        if self.ether_object.ispicked and self.tube_object.ispicked and self.needle_object.ispicked :
            print("---- Congratulation you win the game ----")
        else :
            print("---- Sorry, You loose, you don't have all the required items")

if __name__ == "__main__":
    test = Motor()