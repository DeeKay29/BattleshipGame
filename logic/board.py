import json
import os
import random
from .ship import Ship
from termcolor import colored

class Board:
    def __init__(self):
        # Load game parameters from JSON file
        game_parameters_path = os.path.join(os.getcwd(), 'static', 'data', 'gameParameters.json')
        with open(game_parameters_path) as f:
            game_parameters = json.load(f)

        # Get game parameters
        self.headers = game_parameters["board headers"]
        self.board_size = game_parameters["game board size"]
        self.turns = game_parameters["turns"]

        # Create an empty board
        self.board = []
        for row_idx, row_header in enumerate(self.headers["rows"]):
            row = []
            for col_idx, col_header in enumerate(self.headers["columns"]):
                cell_id = col_header + row_header + str(col_idx + 1)
                row.append({'id': cell_id, 'ship': None, 'hit': False})
            self.board.append(row)

        # Create a list of ships
        self.ships_list = game_parameters["ships"]
        self.ships = []
        for ship_type, ship_data in self.ships_list.items():
            for i in range(ship_data['quantity']):
                # Create a ship object
                ship = Ship(ship_type, ship_data["size"])

                # Place the ship on the board
                self.place_ships(ship_type)

                # Add the ship to the list of ships
                self.ships.append(ship)

    def generate_ship_location(self, ship_data):
        # Generate a random location and direction for a given ship
        size = ship_data['size']
        while True:
            direction = random.choice(['horizontal', 'vertical'])
            
            if direction == 'horizontal':
                x = random.randint(0, self.board_size - 1 - size)
                y = random.randint(0, self.board_size - 1)
            else:
                x = random.randint(0, self.board_size - 1)
                y = random.randint(0, self.board_size - 1 - size)

            return x, y, direction

    def generate_ship_coordinates(self, ship_data):
        size = ship_data['size']
        x, y, direction = self.generate_ship_location(ship_data)

        # Generate the coordinates of the ship based on the given location
        if direction == 'horizontal':
            for i in range(x, x + size):
                # Check that the ship does not touch the corners or sides
                conditions = [
                    self.board[y][i]['ship'] is not None,
                    x > 0 and self.board[y][i - 1]['ship'] is not None,
                    x > 0 and y > 0 and self.board[y - 1][i - 1]['ship'] is not None,
                    x < self.board_size - 1 and self.board[y][i + 1]['ship'] is not None,
                    x < self.board_size - 1 and y > 0 and self.board[y - 1][i + 1]['ship'] is not None,
                    y < self.board_size - 1 and self.board[y + 1][i]['ship'] is not None,
                    y < self.board_size - 1 and x > 0 and self.board[y + 1][i - 1]['ship'] is not None,
                    y < self.board_size - 1 and x < self.board_size - 1 and self.board[y + 1][i + 1]['ship'] is not None
                ]
                if any(conditions):
                    return self.generate_ship_coordinates(ship_data)
                self.board[y][i]['ship'] = {'type': ship_data['name'], 'size': ship_data['size']}
        else:
            for j in range(y, y + size):
                # Check that the ship does not touch the corners or sides
                conditions = [
                    self.board[j][x]['ship'] is not None,
                    y > 0 and self.board[j - 1][x]['ship'] is not None,
                    x > 0 and y > 0 and self.board[j - 1][x - 1]['ship'] is not None,
                    y < self.board_size - 1 and self.board[j + 1][x]['ship'] is not None,
                    x > 0 and y < self.board_size - 1 and self.board[j + 1][x - 1]['ship'] is not None,
                    x < self.board_size - 1 and self.board[j][x + 1]['ship'] is not None,
                    y < self.board_size - 1 and x < self.board_size - 1 and self.board[j + 1][x + 1]['ship'] is not None,
                    j > 0 and x < self.board_size - 1 and self.board[j - 1][x + 1]['ship'] is not None
                ]
                if any(conditions):
                    return self.generate_ship_coordinates(ship_data)
                self.board[j][x]['ship'] = {'type': ship_data['name'], 'size': ship_data['size']}

        return x, y, direction

    def place_ships(self, ships):
        # Places all the ships on the board
        for ship in ships:
            attempts = 0
            while attempts < 10:
                try:
                    coordinates = self.generate_ship_coordinates(ship_data=ship)
                    self.add_ship(ship, coordinates)
                    break
                except Exception as e:
                    print(colored(f'An error occurred: {e}', 'red'))
                    attempts += 1
            else:
                print(colored(f'Could not place ship on the board. Skipping...', 'yellow'))
                continue
            print('Ship placed on the board successfully.')