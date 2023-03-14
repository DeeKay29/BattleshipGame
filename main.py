import json, sys
import termcolor as colored
from beautifultable import BeautifulTable as table

# TODO: Display rules
def display_rules():
    pass

# TODO: Check if user is ready

# Define game parameters
try:
    with open('./data/gameParameters.json', 'r') as f:
        game_parameters = json.load(f)
        col_headers = game_parameters.get('boardHeaders', {}).get('columns', [])
        row_headers = game_parameters.get('boardHeaders', {}).get('rows', [])
        ship_number = game_parameters.get('shipNumb', {})
        game_board_size = game_parameters.get('gameBoardSize')
        # TODO: Add turns
except FileNotFoundError:
    print(colored('Error: ', 'red', attrs=['bold']) + colored('File not found. ', 'red') + 'Please make sure the `boardHeaders.json` file exists.')
    sys.exit()
except json.JSONDecodeError:
    print(colored('Error: ', 'red', attrs=['bold']) + colored('JSON decoding error. ', 'red') + 'Please check the data in the `boardHeaders.json` file.')
    sys.exit()

# Create empty game board
def create_game_board(game_board_size, col_headers, row_headers):
    # Create table
    game_board = table()

    # Create headers
    game_board.columns.header = col_headers
    game_board.rows.header = row_headers
    
    # Create board
    for i in range(game_board_size):
        game_board.rows[i] = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    
    print(game_board)

create_game_board(game_board_size, col_headers, row_headers)

# TODO: Create ships
def create_ships():
    pass

# TODO: Generate ship location
def get_ship_location():
    pass

# TODO: Count hit ships
def count_hit_ships():
    pass