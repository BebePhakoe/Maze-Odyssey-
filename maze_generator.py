import json
import random

def generate_maze(rows, cols):
    # Your maze generation algorithm here
    maze = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
    return maze

def save_maze_to_json(maze_data, filename):
    with open(filename, 'w') as f:
        json.dump(maze_data, f)

def load_maze_from_json(filename):
    with open(filename, 'r') as f:
        maze_data = json.load(f)
    return maze_data
