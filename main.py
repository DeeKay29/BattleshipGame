import json, sys, random, warnings
from termcolor import colored
from beautifultable import BeautifulTable as table

# Ignore warning
warnings.filterwarnings("ignore", message="'BeautifulTable.__getitem__' has been deprecated")
warnings.filterwarnings("ignore", message="'BeautifulTable.__len__' has been deprecated")

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

# Display rules
def display_rules():
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
            print('Invalid input. Insert one character (Y / N).')

    # Display difficulty level rules
    for rule in game_rules['difficulty level rules']:
        print(colored(rule, "blue"))

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
            if (
                # Checking cell
                ships_board[i][y] != ' '

                # Checking left side
                or (x > 0 and ships_board[i-1][y] != ' ')

                # Checking left top corner
                or (x > 0 and y > 0 and ships_board[i-1][y-1] != ' ')

                # Checking top side
                or (y > 0 and ships_board[i][y-1] != ' ')

                # Checking top right corner
                or (y > 0 and x + ship_size - 1 < len(ships_board) and ships_board[i+1][y-1] != ' ')

                # Checking right side
                or (x + ship_size - 1 < len(ships_board) and ships_board[i+1][y] != ' ')

                # Checking bottom right corner
                or (x + ship_size - 1 < len(ships_board) and y < len(ships_board) - 1 and ships_board[i+1][y+1] != ' ')

                # Checking bottom side
                or (y < len(ships_board) - 1 and ships_board[i][x+1] != ' ')

                # Checking bottom left corner
                or (x > 0 and y < len(ships_board) - 1 and ships_board[i-1][y-1] != ' ')
            ):
                return False, None
        return True, [(i, y) for i in range(x, x + ship_size)]
    else:
        for i in range(y, y + ship_size):
            if (
                # Checking cell
                ships_board[x][i] != ' '

                # Checking left side
                or (x > 0 and ships_board[x][i] != ' ')

                # Checking top left corner
                or (x > 0 and y > 0 and y > 0 and ships_board[x-1][i-1] != ' ')

                # Checking top side
                or (y > 0 and ships_board[x][i-1] != ' ')

                # Checking top right corner
                or (y > 0 and x < len(ships_board) - 1 and ships_board[x+1][i-1] != ' ')

                # Checking right side
                or (x < len(ships_board) - 1 and ships_board[x+1][i] != ' ')

                # Checking bottom right corner
                or (x < len(ships_board) - 1 and y + ship_size -1 < len(ships_board) - 1 and ships_board[x+1][i+1] != ' ')

                # Checking bottom side
                or (y + ship_size - 1 < len(ships_board) - 1 and ships_board[x][i+1] != ' ')

                # Checking bottom left corner
                or (x > 0 and y < len(ships_board) - 1 and ships_board[x-1][i+1] != ' ')
            ):
                return False, None
        return True, [(x, i) for i in range(y, y + ship_size)]

# Place ships
def place_ships_on_board():
    # Define ship board
    ships_board = create_game_board(game_board_size, col_headers, row_headers)

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

            while not location_found and attempts < 100:
                is_free, coordinates = generate_ships_coordinates(ship['name'], ships_board, ships.get(ship['name'], {}).get('size'))

                if is_free:
                    for coordinate in coordinates:
                        x, y = coordinate
                        ships_board[x][y] = 's'
                    location_found = True
                else:
                    attempts += 1

            if attempts == 100:
                print(colored("Error: ", "red", attrs=['bold']) + colored("Unable to place all ships on board. Please try again.", "red"))
                sys.exit()

    # Return board with ships
    return ships_board

# Convert coordinates
def convert_coordinates(coordinates):
    # Check string length
    if (len(coordinates) == 2 or len(coordinates) == 3):
        # Split string 
        x = coordinates[0]
        y = coordinates[1:]

        # Check if x and y format is valid
        if x in col_headers and y in row_headers:
            x = ord(x) - ord('A')
            y = int(y) - 1
            return True, x, y
        else:
            return False, None, None
    else:
        return False, None, None

# Game logic
def game(game_turns):
    # Generate new ships board and player board
    ships_board = place_ships_on_board()
    player_board = create_game_board(game_board_size, col_headers, row_headers)

    # Display rules
    display_rules()

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

    # Define game starting parameters
    hits = 0

    # Display player board
    print(colored("Let's begin. Here os your board. When you take a shot, we'll mark its position on it.", 'blue'))
    print(player_board)

    # Game loop
    while hits < 20 and turns > 0:
        # Ask user for coordinates
        coordinates = input("Admiral, enter coordinates to shoot (e.g. D2): ")
        is_valid_coordinates, x, y = convert_coordinates(coordinates)

        # Check if coordinates are valid
        if is_valid_coordinates == False:
            print(colored("Invalid coordinates. Please try again.", 'red'))
            continue

        # Check if position has already been hit
        if player_board[x][y] != ' ':
            print(colored("Your already shot there. Please try again.", 'red'))
            continue

        # Check if position is a hit or a miss
        if ships_board[x][y] == 's':
            print(colored("HIT! ", 'green', attrs=['bold']) + colored("Excellent work admiral. Opponents are in fear.", 'green'))
            player_board[x][y] = 'o'
            hits += 1
        else:
            print(colored("MISS! ", 'yellow', attrs=['bold']) + colored("Maybe next time you'll make it.", 'yellow'))
            player_board[x][y] = 'x'

        # Display player board with updated shot
        print(player_board)

        # Decrease number of turns
        turns -= 1

    # Game over
    if hits == 20:
        print(colored("Congratulations! You sunk all the ships and won the game!", 'green'))
    else:
        print(colored("Sorry, you ran out of turns. Game over.", 'red'))

game(game_turns)