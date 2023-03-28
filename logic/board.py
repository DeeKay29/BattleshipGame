import json
import os
import random
from .ship import Ship

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
        self.ships_list = []
        for ship_type, ship_data in self.ships.items():
            for i in range(ship_data['quantity']):
                # Create a ship object
                ship = Ship(ship_type, ship_data["size"])

                # Place the ship on the board
                self.place_ship(ship)

                # Add the ship to the list of ships
                self.ships_list.append(ship)

    def generate_ship_location(self, ship):
        # Generate a random location and direction for a given ship
        size = ship.size
        while True:
            direction = random.choice(['horizontal', 'vertical'])
            
            if direction == 'horizontal':
                x = random.randint(0, self.board_size - 1 - size)
                y = random.randint(0, self.board_size - 1)
            else:
                x = random.randint(0, self.board_size - 1)
                y = random.randint(0, self.board_size - 1 - size)

            return x, y, direction

    def generate_ship_coordinates(self, ship):
        size = ship.size
        x, y, direction = self.generate_ship_location()
        # Generate the coordinates of the ship based on given location
        if direction == 'horizontal':
            for i in range(x, x + size):
                # Check that the ships do not touch corners and sides
                conditions = [
                    self.board[y][i]['ship'] is not None,
                    x > 0 and self.board[y][i-1] is not None,
                    x > 0 and y > 0 and self.board[y-1][i-1] is not None,
                    y > 0 and self.board[y-1][i] is not None,
                    y > 0 and x + size - 1 < len(self.board) and self.board[y-1][i+1] is not None,
                    x + size - 1 < len(self.board) and self.board[y][i+1] is not None,
                    x + size - 1 < len(self.board) and y < len(self.board) - 1 and self.board[y+1][i+1] is not None,
                    y < len(self.board) - 1 and self.board[y+1][i] is not None,
                    x > 0 and y < len(self.board) - 1 and self.board[y-1][i-1] is not None
                ]
                if any(conditions):
                    return False, None
                else:
                    return True, [(i, y) for i in range (x, x + size)]
        else:
            for i in range(y, y + size):
                # Check that the ships do not touch corners and sides
                conditions = [
                    self.board[i][x] is not None,
                    x > 0 and self.board[i][x-1] is not None,
                    x > 0 and y > 0 and self.board[i-1][x-1] is not None,
                    y > 0 and self.board[i-1][x] is not None,
                    y < 0 and x < len(self.board) - 1 and self.board[i-1][x+1] is not None,
                    x < len(self.board) - 1 and self.board[i][x+1] is not None,
                    x < len(self.board) - 1 and y + size - 1 < len(self.board) - 1 and self.board[i+1][x+1] is not None,
                    y + size - 1 < len(self.board) - 1 and self.board[i+1][x] is not None,
                    x > 0 and y < len(self.board) - 1 and self.board[i+1][x-1] is not None
                ]
                if any(conditions):
                    return False, None
                else:
                    return True, [(x, i) for i in range(y, y + size)]

    def place_ship(self):
        # Place the ship on the board
        for ship in self.ships_list:
            for i in range():
                location_found = False
                attempts = 0

            while not location_found and attempts < 100:
                is_free, coordinates = self.generate_ship_coordinates()
                
                if is_free:
                    for coordinate in coordinates:
                        x, y = coordinate
                        # TODO : Join x and y in ID
                        # TODO : Update the cell
                    location_found = True
                else:
                    attempts += 1
                    
            if attempts == 100:
                # TODO : Clear board
                # TODO : Place ships again
                pass