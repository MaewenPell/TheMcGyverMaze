from const import MC_GYVER
import sys

class McGyver():
    def __init__(self):
        self.mc_gyver = MC_GYVER
    def str_repr(self):
        return MC_GYVER
    def next_move(self, mc_gyver_pos, maze):

        ''' We determine if the next move is possible or not '''

        ''' We get the x,y coordinate of McGyver '''
        x_coords = mc_gyver_pos[0]
        y_coords = mc_gyver_pos[1]

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
                if self.is_crossable_or_picked(self.maze[MOVE_N]):
                    self.maze[MOVE_N], self.maze[self.mc_gyver_pos] = self.maze[self.mc_gyver_pos], self.maze[MOVE_N]
                    self.mc_gyver_pos = MOVE_N  # We assign the new position
                else:
                    print("Sorry this move is impossible")
            except KeyError:
                print("Sorry this move is impossible you get out of the maze")
                user_move = input(
                    "Entrez votre next move currently (n/s/e/o) -q : ")
        elif (user_move == "s"):
            try:
                if self.is_crossable_or_picked(self.maze[MOVE_S]):
                    self.maze[MOVE_S], self.maze[self.mc_gyver_pos] = self.maze[self.mc_gyver_pos], self.maze[MOVE_S]
                    self.mc_gyver_pos = MOVE_S
                else:
                    print("Sorry this move is impossible")
            except KeyError:
                print("Sorry this move is impossible you get out of the maze")
                user_move = input(
                    "Entrez votre next move currently (n/s/e/o) -q : ")
        elif (user_move == "e"):
            try:
                if self.is_crossable_or_picked(self.maze[MOVE_E]):
                    self.maze[MOVE_E], self.maze[self.mc_gyver_pos] = self.maze[self.mc_gyver_pos], self.maze[MOVE_E]
                    self.mc_gyver_pos = MOVE_E
                else:
                    print("Sorry this move is impossible")
            except KeyError:
                print("Sorry this move is impossible you get out of the maze")
                user_move = input(
                    "Entrez votre next move currently (n/s/e/o) -q : ")
        elif (user_move == "o"):
            try:
                if self.is_crossable_or_picked(self.maze[MOVE_O]):
                    self.maze[MOVE_O], self.maze[self.mc_gyver_pos] = self.maze[self.mc_gyver_pos], self.maze[MOVE_O]
                    self.mc_gyver_pos = MOVE_O
                else:
                    print("Sorry this move is impossible")
            except KeyError:
                print("Sorry this move is impossible you get out of the maze")
                user_move = input(
                    "Entrez votre next move currently (n/s/e/o) -q : ")
        else:
            print(
                "Wrong you didn't enter a correct direction please enter (n/s/e/o) or (q) to quit")