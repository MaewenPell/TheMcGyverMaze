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
- Press 'r' to restart or 'q' to leave the game

Note : You can quit the game all the time by pressing 'esc'

### Modification of the map 

If you want modify the map you can do it easily by downloading the little soft Tiled map editor :
(https://www.mapeditor.org/) 

1st step - Open the current tmx file located in the maps folder
2nd step - If you want to delete walls :
            1 - Click on the wall layer
            2 - Click on the eraser(E)
            3 - Click on the walls you want to delete
![alt text](https://ibb.co/LJkVXbD)

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

