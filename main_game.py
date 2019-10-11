import os
import sys
from lab import Maze

def load_game():
    '''We load the txt map and we transform it on object Maze'''
    get_dir = os.path.dirname(os.path.abspath(__file__)) #Get the full path from where we execute the script
    with open(get_dir + '/map.txt') as fichier:
        current_map = fichier.read()
    maze = Maze('O','X','U','&',current_map) #We assign the char for the diffrents elem of the maze
    return maze

def next_move(maze, current_position, maze_width):
    user_move = input("Entrez votre next move currently (n/s/e/o) -q : ")
    if (user_move == "q"):
        sys.exit(0)
    if (user_move == "n"):
            move_attempt = current_position - (maze_width + 1)
            if maze.is_crossable(maze.current_map[move_attempt]):
                map_processessing(maze.current_map,
                                  maze.current_position, move_attempt)
            else :
                print("Deplacement impossible")
    elif (user_move == "e"):
            move_attempt = maze.current_position + 1
            if maze.is_crossable(maze.current_map[move_attempt]):
                map_processessing(maze.current_map, maze.current_position, move_attempt)
            else:
                print("Deplacement impossible")
    elif (user_move == "o"):
            move_attempt = maze.current_position - 1
            if maze.is_crossable(maze.current_map[move_attempt]):
                map_processessing(maze.current_map,
                                  maze.current_position, move_attempt)
            else:
                print("Deplacement impossible")
    elif (user_move == "s"):
            move_attempt = maze.current_position + (maze_width + 1)
            if maze.is_crossable(maze.current_map[move_attempt]):
                map_processessing(maze.current_map,
                                  maze.current_position, move_attempt)
            else:
                print("Deplacement impossible")
    else :
        print("Wrong you didn't enter a valid move")
    
def map_processessing(current_map, current_position, move_attempt):
    ''' We swap two elem, the orignal place and the destination like [a],[b] = [b],[a]'''
    maze.current_map = list(maze.current_map) #need to make a list in order to assign values
    maze.current_map[current_position], maze.current_map[move_attempt] = maze.current_map[move_attempt], maze.current_map[current_position]
    print(maze.current_map)
    maze.current_map = ''.join(maze.current_map) #we join to have a good visual
    maze.current_position = move_attempt #actualisation of the position after move

if __name__ == "__main__":
    maze = load_game()
    maze_width = 0
    while(maze.current_map[maze_width] != '\n'):
        maze_width += 1
    print(maze.current_map)
    #print("Before the moves : \n The current position is {}".format(maze.current_position))
    while(maze.current_position != maze.iswin):
        next_move(maze, maze.current_position, maze_width)
        print("************* ACTUALISED MAP ***********")
        print(maze.current_map)
        #print("After the moves : \n The current position is {}".format(maze.current_position))
