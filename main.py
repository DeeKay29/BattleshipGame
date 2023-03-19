import json, sys, random
from termcolor import colored
from beautifultable import BeautifulTable as table

# Define game rules
try:
    with open('./data/gameRules.json', 'r') as f:
        game_rules = json.load(f)
except FileNotFoundError:
    print(colored('Error: ', 'red', attrs=['bold']) + colored('File not found. ', 'red') + 'Please make sure the `gameRules.json` file exists.')
    sys.exit()
except json.JSONDecodeError:
    print(colored('Error: ', 'red', attrs=['bold']) + colored('JSON decoding error. ', 'red') + 'Please check the data in the `gameRules.json` file.')
    sys.exit()

# Display general rules
for rule in game_rules['general rules']:
    print(colored(rule, "blue"))

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
    print(colored(rule, "blue"))

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

# Generate ships location
def generate_ships_location(ships, ship_name):
    while True:
        # Randomly choose orientation
        orientation = random.choice(['horizontal', 'vertical'])

        # Randomly choose starting point coordinates
        if orientation == 'horizontal':
            x = random.randint(0, 9 - ships.get(ship_name, {}).get('size'))
            y = random.randint(0, 9)
        else:
            x = random.randint(0, 9)
            y = random.randint(0, 9 - ships.get(ship_name, {}).get('size'))

        # Return ship location
        return x, y, orientation

# Generate ships coordinates and check if location is free
def generate_ships_coordinates(ship_name, ships_board, ship_size):
    # Generate ship location
    x, y, orientation = generate_ships_location(ships, ship_name)

    # Generate ship coordinates
    if orientation == 'horizontal':
        for i in range(x, x + ship_size):
            if ships_board[y][i] != ' ':
                return False, None
        return True, [(i, y) for i in range(x, x + ship_size)]
    else:
        for i in range(y, y + ship_size):
            if ships_board[i][x] != ' ':
                return False, None
        return True, [(x, i) for i in range(y, y + ship_size)]

# Place ships
def place_ships_on_board():
    # Define ship board
    ships_board = create_game_board(game_board_size, col_headers, row_headers);

    # Define ships list
    ships_list = [
        {'name': 'single masted'},
        {'name': 'two masted'},
        {'name': 'three masted'},
        {'name': 'four masted'},
    ]

    # PLace ships on board
    for ship in ships_list:
        for i in range(ships.get(ship['name'], {}).get('quantity')):
            location_found = False
            attempts = 0

            while not location_found and attempts < 40:
                is_free, coordinates = generate_ships_coordinates(ship['name'], ships_board, ships.get(ship['name'], {}).get('size'))

                if is_free:
                    for coordinate in coordinates:
                        x, y = coordinate
                        ships_board[x][y] = 's'
                    location_found = True
                else:
                    attempts += 1

            if attempts == 40:
                print(colored("Error: ", "red", attrs=['bold']) + colored("Unable to place all ships on board. Please try again.", "red"))
                sys.exit()

    # Return board with ships
    print(ships_board)

place_ships_on_board()

# Game logic
def game():
    # TODO : Ask user for coordinates
        # TODO : Check if user input is valid
        # TODO : Split user input into coordinates
        # TODO : Change letter to a number
        # TODO : Assign x and y coordinates
    # TODO : Compere the x and y position with the ships board
        # TODO : if [x][y] = 's' => positive, return game board with green 'o' symbol
        # TODO : if [x][y] = ' ' => negative, return game board with red 'x' symbol
        # TODO : decrease turn number
    # TODO : Check if the positions of the 'o' symbols on the game board match the 's' symbols on the ship board
        # TODO : if all 'o' == 's' => win
        # TODO : else ==> continue
    # TODO : Check if turn == 0
        # TODO : if turn == 0 => game over
        # TODO : else ==> continue
    pass