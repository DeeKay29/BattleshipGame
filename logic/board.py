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

    def generate_ship_coordinates(self,ship):
        size = ship.size
        x, y, direction = self.generate_ship_location()
        # Generate the coordinates of the ship based on given location
        if direction == 'horizontal':
            for i in range(x, x + size):
                # Check that the ships do not touch corners and sides
                conditions = [
                    # TODO : Add conditions if horizontal
                ]
                if any(conditions):
                    return True, [(i, y) for i in range (x, x + size)]
                else:
                    return False, None
        else:
            for i in range(y, y + size):
                # Check that the ships do not touch corners and sides
                conditions = [
                    # TODO: Add conditions if vertical
                ]
                if any(conditions):
                    return True, [(x, i) for i in range(y, y + size)]
                else:
                    return False, None

    def place_ship(self):
        # Place the ship on the board
        pass