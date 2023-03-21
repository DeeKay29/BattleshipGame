import json
import sys
from termcolor import colored

class GameParameters:
    def __init__(self, filepath='./data/game_data/gameParameters.json'):
        self.filepath = filepath
        try:
            with open(self.filepath, 'r') as f:
                game_parameters = json.load(f)
                self.col_headers = game_parameters.get('board headers', {}).get('columns', [])
                self.row_headers = game_parameters.get('board headers', {}).get('rows', [])
                self.ships = game_parameters.get('ships', {})
                self.game_board_size = game_parameters.get('game board size')
                self.max_turns = game_parameters.get('turns', {})
        except FileNotFoundError:
            print(colored('Error: ', 'red', attrs=['bold']) + colored('File not found. ', 'red') + 'Please make sure the `boardHeaders.json` file exists.')
            sys.exit()
        except json.JSONDecodeError:
            print(colored('Error: ', 'red', attrs=['bold']) + colored('JSON decoding error. ', 'red') + 'Please check the data in the `boardHeaders.json` file.')
            sys.exit()

    def get_col_headers(self):
        return self.col_headers

    def get_row_headers(self):
        return self.row_headers

    def get_ships(self):
        return self.ships

    def get_game_board_size(self):
        return self.game_board_size

    def get_max_turns(self):
        return self.max_turns