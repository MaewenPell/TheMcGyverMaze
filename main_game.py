import os
import sys
from lab import Maze
from const import WALL, MC_GYVER, START, END, FLOOR, WIDTH, ENTER


class Motor():
    '''Class who will handle the execution of the game '''

    def __init__(self):
        '''We load the file countaining the map'''
        get_dir = get_dir = os.path.dirname(os.path.abspath(__file__))
        with open(get_dir + '/map.txt') as fichier:
            txt_map = fichier.read()

        ''' We call the differents method of the class '''

        maze = self.maze_generator(txt_map) #maze is a dict obj
        self.display_maze(maze)
        self.labyrinthe(WALL, ENTER, END, MC_GYVER, maze)

    def labyrinthe(self, wall, enter, exit_door, player, txt_map):
        ''' We determine wall, enter, exit_door, player, current_map(txt file)'''
        self.wall = wall
        self.enter = enter
        self.exit_door = exit_door
        self.player = player
        self.txt_map = txt_map

    def maze_generator(self, txt_map):
        x = 0
        y = 0
        labyrinthe_map = {}
        for elem in txt_map:
            if x is not '\n':
                labyrinthe_map[(x, y)] = elem
                x += 1
            else :
                x = 0
                y += 1
        return labyrinthe_map

    def is_crossable(self, element):
        ''' Return true or false depending of the element founded '''
        if element == self.wall:
            return False
        elif element == self.enter:
            return True
        elif element == self.exit_door:
            return True
        else :
            return True

    def display_maze(self, labyrinthe_map):
        print(''.join(labyrinthe_map.values()))

    # def next_move(self, maze, current_position, maze_width):
    #     user_move = input("Entrez votre next move currently (n/s/e/o) -q : ")
    #     if (user_move == "q"):
    #         sys.exit(0)
    #     if (user_move == "n"):
    #             move_attempt = current_position - (maze_width + 1)
    #             if maze.is_crossable(maze.current_map[move_attempt]):
    #                 map_processessing(maze.current_map,
    #                                 maze.current_position, move_attempt)
    #             else :
    #                 print("Deplacement impossible")
    #     elif (user_move == "e"):
    #             move_attempt = maze.current_position + 1
    #             if maze.is_crossable(maze.current_map[move_attempt]):
    #                 map_processessing(maze.current_map, maze.current_position, move_attempt)
    #             else:
    #                 print("Deplacement impossible")
    #     elif (user_move == "o"):
    #             move_attempt = maze.current_position - 1
    #             if maze.is_crossable(maze.current_map[move_attempt]):
    #                 map_processessing(maze.current_map,
    #                                 maze.current_position, move_attempt)
    #             else:
    #                 print("Deplacement impossible")
    #     elif (user_move == "s"):
    #             move_attempt = maze.current_position + (maze_width + 1)
    #             if maze.is_crossable(maze.current_map[move_attempt]):
    #                 map_processessing(maze.current_map,
    #                                 maze.current_position, move_attempt)
    #             else:
    #                 print("Deplacement impossible")
    #     else :
    #         print("Wrong you didn't enter a valid move")
    
    # def map_processessing(current_map, current_position, move_attempt):
    #     ''' We swap two elem, the orignal place and the destination like [a],[b] = [b],[a]'''
    #     maze.current_map = list(maze.current_map) #need to make a list in order to assign values
    #     maze.current_map[current_position], maze.current_map[move_attempt] = maze.current_map[move_attempt], maze.current_map[current_position]
    #     print(maze.current_map)
    #     maze.current_map = ''.join(maze.current_map) #we join to have a good visual
    #     maze.current_position = move_attempt #actualisation of the position after move

if __name__ == "__main__":
    test = Motor()

# maze = load_game()
# maze_width = 0
# while(maze.current_map[maze_width] != '\n'):
#     maze_width += 1
# print(maze.current_map)
# #print("Before the moves : \n The current position is {}".format(maze.current_position))
# while(maze.current_position != maze.iswin):
#     next_move(maze, maze.current_position, maze_width)
#     print("************* ACTUALISED MAP ***********")
#     print(maze.current_map)
#     #print("After the moves : \n The current position is {}".format(maze.current_position))
