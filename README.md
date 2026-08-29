# Maze Algorithms

Algorithms to generate mazes and to find the shortest solution to them. Written in python and visualized with pygame.
*recursive backtracker*
---

<img width="901" height="901" alt="image" src="https://github.com/user-attachments/assets/3ebacca4-81b3-4775-acba-acf614ef0194" />

## About the Project

To create the maze there is a recursive backtracker and to find a solution there is a wall follower and dead end fillings algorithm. The recursive backtracker saves the maze as a json file and this file is loaded in by the other two. Mazes are stored as pure lists with booleans, for each cell in there is a boolean for wether or not there is a wall above the cell and wether or not there is one left of it. For each file there is two versions: a normal and a big one. The normal one is a maze of 30 by 30 cells, the big one 100 by 100. 

I also use the recursive backtracker for [my maze rendering project](https://github.com/IAmDaanE/3d-maze-renderer), it takes that maze and shows it in 3d space so you can walk around in it.

## The Algorithms

#### Recursive Backtracker

Starts in the corner and keeps going in random directions to cells that haven't been visited yet. It 'breaks' the walls where it passes. If it's closed in, meaning all cells around it have already been visited, he will backtrack on his steps until there is another unvisited cell. This continues until all cells have been visited.

#### Wall Follower

Simplest maze solving algorithm out there, its like you walk in a maze and keep following the left wall with your left arm. This creates a possibly incredibly long solution but it always works.

#### Dead End Fillings

Builds up by filling all dead ends. It starts by checking all cells and marking the ones that have 3 walls around it and one opening, this means its a dead end. Then it checks the cells around these marked ones to see if it just created a new dead end. This continues until only one pathway from the start to the exit is remaining.

## Project Status

Describe the current release and any notes about the current state of the project. Examples: currently compiles on your host machine, but is not cross-compiling for ARM, APIs are not set, feature not implemented, etc.

## Getting Started

### Getting the Source

This project is [hosted on GitHub](https://github.com/IAmDaanE/maze-algorithms). You can download the zip or clone this project directly using this command:

```
git clone git@github.com:IAmDaanE/maze-algorithms.git
```

### Running the Program

Requirements: You must have Python 3.6 - 3.13.
1. Clone the repository or download the zip and unpack it to your directory of choice.
2. Navigate to that directory in a terminal.
3. In a venv or the global python version install the needed libraries.
    ```
    pip install -r requirements.txt
    ```
4. Run the program.
    ```
    python src/recursive_backtracker.py
    ```

## License

This project is open-source and available under the MIT License.
