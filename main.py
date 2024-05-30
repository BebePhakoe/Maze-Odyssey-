from maze_generator import generate_maze, save_maze_to_json, load_maze_from_json
from game_logic import Game
from game_interface import GameInterface

def main():
    maze_data = generate_maze(10, 10)  # Example maze generation
    save_maze_to_json(maze_data, 'maze.json')  # Save maze to JSON file
    maze_data = load_maze_from_json('maze.json')  # Load maze from JSON file

    game = Game(maze_data)
    interface = GameInterface(800, 600)

    while True:
        interface.handle_events()
        game.update()
        interface.draw_maze(maze_data)
        interface.draw_player(game.player)
        interface.update_display()

if __name__ == "__main__":
    main()
