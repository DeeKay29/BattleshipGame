import json, sys, random
import termcolor as colored
from beautifultable import BeautifulTable as table

# Define game rules
try:
    with open('./data/gameRules.json', 'r') as f:
        game_rules = json.load(f)
except FileNotFoundError:
    print(colored('Error: ', 'red', attrs=['bold']) + colored('File not found. ', 'red') + 'Please make sure the `boardHeaders.json` file exists.')
    sys.exit()
except json.JSONDecodeError:
    print(colored('Error: ', 'red', attrs=['bold']) + colored('JSON decoding error. ', 'red') + 'Please check the data in the `boardHeaders.json` file.')
    sys.exit()

# Display general rules
for rule in game_rules['general rules']:
    print(rule)

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
        col_headers = game_parameters.get('board headers', {}).get('columns', [])
        row_headers = game_parameters.get('board headers', {}).get('rows', [])
        ships = game_parameters.get('ships', {})
        game_board_size = game_parameters.get('game board size')
        game_turns = game_parameters.get('turns', {})
except FileNotFoundError:
    print(colored('Error: ', 'red', attrs=['bold']) + colored('File not found. ', 'red') + 'Please make sure the `boardHeaders.json` file exists.')
    sys.exit()
except json.JSONDecodeError:
    print(colored('Error: ', 'red', attrs=['bold']) + colored('JSON decoding error. ', 'red') + 'Please check the data in the `boardHeaders.json` file.')
    sys.exit()

# Display difficulty level rules
for rule in game_rules['difficulty level rules']:
    print(rule)

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
    
    # Return game_board
    return(game_board)

create_game_board(game_board_size, col_headers, row_headers)

# Generate ships location
def generate_ships_location(ships, ship_name):
    while True:
        # Randomly choose orientation
        orientation = random.choice(['horizontal', 'vertical'])
        
        # Randomly choose coordinates
        if orientation == 'horizontal':
            x = random.randint(0, 9 - ships.get(ship_name, {}).get('size'))
            y = random.randint(0, 9)
        else:
            x = random.randint(0, 9)
            y = random.randint(0, 9 - ships.get(ship_name, {}).get('size'))

        # Return ship coordinates
        return x, y, orientation

# Check if location is free
def is_location_free(ships_board, x, y):
    # Check if cells are free
    # Check if around are free cells
    return True

# Generate ships
def generate_ships_on_board(game_board, ships, x, y, orientation):
    # Define ship board
    ships_board = game_board;
    
    # Generate single masted
    for i in range(1, ships.get('single masted').get('quantity') + 1):
        # Generate ship location
        generate_ships_location(ships, 'single masted')
        
        # Check if location is free
        if is_location_free(ships_board, x, y) == True:
            pass
        else:
            pass

    # Generate two masted
    # Generate three masted
    # Generate four masted
    # Return second board (with ships)
    return(ships_board)

def game():
    pass