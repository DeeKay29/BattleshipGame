import json, sys, random
from termcolor import colored
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

        # Randomly choose starting point coordinates
        if orientation == 'horizontal':
            x = random.randint(0, 9 - ships.get(ship_name, {}).get('size'))
            y = random.randint(0, 9)
        else:
            x = random.randint(0, 9)
            y = random.randint(0, 9 - ships.get(ship_name, {}).get('size'))

        # Return ship location
        return x, y, orientation

# Generate ships coordinates
def generate_ships_coordinates(ship_name):
    # Generate ship location
    x, y, orientation = generate_ships_location(ships, ship_name)

    # Generate all ship coordinates
    if orientation == 'horizontal':
        # Set the initial value for x
        x_start = x

        # Set the final value for x
        x_stop = x_start + ships.get(ship_name, {}).get('size')

        # Create an array of coordinates
        coordinates = []

        # Add a tuple with coordinates to the array
        for x in range(x_start, x_stop):
            coordinates.append((x, y))

        # Return coordinates
        return coordinates
    else:
        # Set the initial value for y
        y_start = y

        # Set the final value for y
        y_stop = y_start + ships.get(ship_name, {}).get('size')

        # Create an array of coordinates
        coordinates = []

        # Add a tuple with coordinates to the array
        for y in range(y_start, y_stop):
            coordinates.append((x, y))

        # Return coordinates
        return coordinates

# Check if location is free
def is_location_free(ships_board, ship_name):
    # Generate ships coordinates
    coordinates = generate_ships_coordinates(ship_name)

    # Check if cells are free
    for coordinate in coordinates:
        if ships_board[coordinate[0]][coordinate[1]] != ' ':
            return False

    # Check if around are free cells
    for coordinate in coordinates:
        x, y = coordinate[0], coordinate[1]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (x+i) in range(10) and (y+j) in range(10):
                    if ships_board[x+i][y+j] != ' ':
                        return False

    return True, coordinates

# Place ships
def place_ships_on_board(game_board):
    # Define ship board
    ships_board = game_board;

    # Place single masted
    for i in range(1, ships.get('single masted', {}).get('quantity') + 1):
        # Check if location is free
        is_free, coordinates = is_location_free(ships_board, 'single masted')
        if is_free == True:
            # Place ships on board
            for coordinate in coordinates:
                x, y = coordinate
                ships_board[x][y] = 's'
        else:
            # TODO : Handle when there is no free location
            pass

    # Place two masted
    for i in range(1, ships.get('two masted', {}).get('quantity') + 1):
        # Check if location is free
        is_free, coordinates = is_location_free(ships_board, 'two masted')
        if is_free == True:
            # Place ships on board
            for coordinate in coordinates:
                x, y = coordinate
                ships_board[x][y] = 's'
        else:
            # TODO : Handle when there is no free location
            pass

    # Place three masted
    for i in range(1, ships.get('three masted', {}).get('quantity') + 1):
        # Check if location is free
        is_free, coordinates = is_location_free(ships_board, 'three masted')
        if is_free == True:
            # Place ships on board
            for coordinate in coordinates:
                x, y = coordinate
                ships_board[x][y] = 's'
        else:
            # TODO : Handle when there is no free location
            pass

    # Place four masted
    for i in range(1, ships.get('four masted', {}).get('quantity') + 1):
        # Check if location is free
        is_free, coordinates = is_location_free(ships_board, 'four masted')
        if is_free == True:
            # Place ships on board
            for coordinate in coordinates:
                x, y = coordinate
                ships_board[x][y] = 's'
        else:
            # TODO : Handle when there is no free location
            pass

    # Return board with ships
    return ships_board

# TODO : Game logic
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