from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_maze', methods=['GET'])
def get_maze():
    """
    Retrieves maze configuration data from JSON files and returns it to the client.
    """
    maze_data = load_maze_from_json()  # Function to load maze data from JSON files
    return jsonify(maze_data)
