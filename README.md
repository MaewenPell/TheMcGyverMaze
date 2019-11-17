# The McGyverMaze

Short python game where we guide a character through a maze. To win the game we need to get three items placed in the maze.

## Getting Started and installation

1st step - Download the repo :
```
git clone https://github.com/MaewenPell/TheMcGyverMaze
```

2nd step - Create a virutal env and activate it
```
virtualenv -r python3 env
source env/bin/activate
```

3rd step - Download the dependencies :
```
pip install -r requirement.txt
```

4th step - Launch the game :
```
python3 pygame_main.py
```


### Prerequisites

If you don't have them you would need :
- PIP to download the dependencies (https://pypi.org/project/pip/)
- Virtualenv to generate a local env to run the game (https://virtualenv.pypa.io/en/stable/installation/)

### Playing

To play the game :

- Arrow keys or (Z/Q/S/D) to move the character through the maze
- Get the three item before facing the boss otherwise you'll loose the game
- When you finish : Press 'r' to restart or 'q' to leave the game

Note : You can quit the game all the time by pressing 'esc'

## Modification of the map 

### If you want modify the map you can do it easily by downloading the little soft Tiled map editor : (https://www.mapeditor.org/)

### Erasing wall : 

1. step - Open the current tmx file located in the maps folder (The_maze_game/maps/map_1.tmx)

1. step - If you want to delete walls : 
    1. - Click on the wall layer (1)
    1. - Click on the eraser (2)
    1. - Erase the walls you want 

Erase walls: ![Erase walls](https://i.postimg.cc/3rGJywSM/Erase.png√)

3. step - Adapt the obstacles layer to the walls:
    1. - Click on the obstacles layer (1)
    1. - Click on Select objects (2)
    1. - Drag the corner of walls adapt the new walls disposition

Adapt layer : ![Adapt layer](https://i.postimg.cc/d3vJG23h/Fit-walls.png)

Fitting done : ![Fitting done](https://i.postimg.cc/rs0FVVDJ/new-fitting.png)

4. step - Save to overite the current tmx file in (The_maze_game/maps/map_1.tmx)

5. Relauch the game and enjoy you modified map ! :)

New map : ![New map](https://i.postimg.cc/02p3FznC/modified-map.png)

## Build Walls

1. Step - Click on the wall layer (1)
1. Step - Select the structure ressource (2)
1. Step - Select the tile you want to add (3)
1. Step - Click on the map where you want to add the wall

Adding walls : ![Addings walls](https://i.postimg.cc/tJhsFdjf/Addings-walls.png)


5. Step - Re-it the obstacle layer : Click on the Obstacles layer (1)
6. Step - Click on Insert rectangle (2)
7. Step - Drag around your new walls(3)
8. Step - Add them as wall - Save and and enjoy you modified map :)

Fitting new walls : ![Fitting add walls](https://i.postimg.cc/jCYnwgnB/adding-walls.png)


## Contributing

Feel free to fork and do whatever you want with this basis :) 

## Authors

* **Maewen PELLETIER** - *Initial work* - [Github](https://github.com/MaewenPell)

## Acknowledgments

* If you have more question or anything feel free to send me a DM :)

