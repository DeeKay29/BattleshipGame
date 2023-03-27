import json
import os
import random
from ship import Ship

class Board:
    def __init__(self):
        game_parameters_path = os.path.join(os.getcwd(), 'static', 'data', 'gameParameters.json')
        with open(game_parameters_path) as f:
            game_parameters = json.load(f)
        self.headers = game_parameters["board headers"]
        self.board_size = game_parameters["game board size"]
        self.turns = game_parameters["turns"]

        self.board = []
        for row_idx, row_header in enumerate(self.headers["rows"]):
            row = []
            for col_idx, col_header in enumerate(self.headers["columns"]):
                cell_id = col_header + row_header + str(col_idx + 1)
                row.append({'id': cell_id, 'ship': None, 'hit': False})
            self.board.append(row)

        self.ships_list = []
        for ship_type, ship_data in self.ships.items():
            for i in range(ship_data['quantity']):
                ship = Ship(ship_type, ship_data["size"])
                self.place_ship(ship)
                self.ships_list.append(ship)

    def generate_ships_location(self, ship):
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

    def generate_ships_coordinates(self):
        pass

    def place_ships(self):
        pass