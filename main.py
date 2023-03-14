import json, sys
import termcolor as colored
from beautifultable import BeautifulTable as table

# Define game rules
try:
    with open('./data/gameRules.json', 'r') as f:
        game_rules = json.load(f)
        general_rules = game_rules.get('generalRules', {})
        difficulty_level_rules = game_rules.get('difficultyLevelRules', {})
except FileNotFoundError:
    print(colored('Error: ', 'red', attrs=['bold']) + colored('File not found. ', 'red') + 'Please make sure the `boardHeaders.json` file exists.')
    sys.exit()
except json.JSONDecodeError:
    print(colored('Error: ', 'red', attrs=['bold']) + colored('JSON decoding error. ', 'red') + 'Please check the data in the `boardHeaders.json` file.')
    sys.exit()

# Display general rules
print('< general rules >')

# Check if user is ready
while True:
    is_user_ready = input('Are you ready admiral? (Y / N):')
    if is_user_ready in ['Y', 'N']:
        if is_user_ready == 'Y':
            break
        elif is_user_ready == 'N':
            print('We are sorry to hear that. See you soon admiral!')
            sys.exit()
        break
    else:
        print('Invalid input. Insert one character (E or M or H).')

# Define game parameters
try:
    with open('./data/gameParameters.json', 'r') as f:
        game_parameters = json.load(f)
        col_headers = game_parameters.get('boardHeaders', {}).get('columns', [])
        row_headers = game_parameters.get('boardHeaders', {}).get('rows', [])
        ships_number = game_parameters.get('shipNumb', {})
        game_board_size = game_parameters.get('gameBoardSize')
        game_turns = game_parameters.get('turns', {})
except FileNotFoundError:
    print(colored('Error: ', 'red', attrs=['bold']) + colored('File not found. ', 'red') + 'Please make sure the `boardHeaders.json` file exists.')
    sys.exit()
except json.JSONDecodeError:
    print(colored('Error: ', 'red', attrs=['bold']) + colored('JSON decoding error. ', 'red') + 'Please check the data in the `boardHeaders.json` file.')
    sys.exit()

# Display difficulty level rules
print('< difficulty level rules >')

# Get difficulty level from a user
while True:
    difficulty_level = input('Choose difficulty level (E / M / H):')
    if difficulty_level in ['E', 'M', 'H']:
        if difficulty_level == 'E':
            turns = game_turns.get('easy')
            break
        elif difficulty_level == 'M':
            turns = game_turns.get('medium')
            break
        elif difficulty_level == 'H':
            turns = game_turns.get('hard')
            break
        break
    else:
        print('Invalid input. Insert one character (E or M or H).')

# Create empty game board
def create_game_board(game_board_size, col_headers, row_headers):
    # Create table
    game_board = table()

    # Create headers
    game_board.columns.header = col_headers
    game_board.rows.header = row_headers
    
    # Create board
    for i in range(game_board_size):
        game_board.rows[i] = list(" " * 10)
    
    print(game_board)

create_game_board(game_board_size, col_headers, row_headers)