import json
import os

class Board:
    def __init__(self):
        game_parameters_path = os.path.join(os.getcwd(), 'static', 'data', 'gameParameters.json')
        with open(game_parameters_path) as f:
            game_parameters = json.load(f)
        self.headers = game_parameters["board headers"]
        self.ships = game_parameters["ships"]
        self.board_size = game_parameters["game board size"]
        self.turns = game_parameters["turns"]

        self.board = []
        for row_idx, row_header in enumerate(self.headers["rows"]):
            row = []
            for col_idx, col_header in enumerate(self.headers["columns"]):
                cell_id = col_header + row_header + str(col_idx + 1)
                row.append({'id': cell_id, 'ship': None, 'hit': False})
            self.board.append(row)