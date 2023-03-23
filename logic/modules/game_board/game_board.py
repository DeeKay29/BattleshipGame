import random
import sys
from beautifultable import BeautifulTable as table
from termcolor import colored
from logic.modules.game_parameters.game_parameters import GameParameters

class GameBoard:
    def __init__(self):
        self.game_board_size = GameParameters().get_game_board_size()
        self.col_headers = GameParameters().get_col_headers()
        self.row_headers = GameParameters().get_row_headers()
        self.ships = GameParameters().get_ships()
        self.board = self.create_game_board()

    # Create empty game board
    def create_game_board(self):
        # Create table
        game_board = table()

        # Create headers
        game_board.columns.header = self.col_headers
        game_board.rows.header = self.row_headers
        
        # Create board
        for i in range(self.game_board_size):
            game_board.rows[i] = list(" " * 10)

        # Return game_board
        return game_board

    # Generate ships location
    def generate_ships_location(self, ship_name):
        while True:
            # Randomly choose orientation
            orientation = random.choice(['horizontal', 'vertical'])

            # Randomly choose starting point coordinates
            if orientation == 'horizontal':
                x = random.randint(0, 9 - self.ships.get(ship_name, {}).get('size'))
                y = random.randint(0, 9)
            else:
                x = random.randint(0, 9)
                y = random.randint(0, 9 - self.ships.get(ship_name, {}).get('size'))

            # Return ship location
            return x, y, orientation

    # Generate ships coordinates and check if location is free
    def generate_ships_coordinates(self, ship_name, ships_board, ship_size):
        # Generate ship location
        x, y, orientation = self.generate_ships_location(ship_name)

        # Generate ship coordinates
        if orientation == 'horizontal':
            for i in range(x, x + ship_size):
                if (
                    # Checking cell
                    ships_board[y][i] != ' '

                    # Checking left side
                    or (x > 0 and ships_board[y][i-1] != ' ')

                    # Checking left top corner
                    or (x > 0 and y > 0 and ships_board[y-1][i-1] != ' ')

                    # Checking top side
                    or (y > 0 and ships_board[y-1][i] != ' ')

                    # Checking top right corner
                    or (y > 0 and x + ship_size - 1 < len(ships_board) and ships_board[y-1][i+1] != ' ')

                    # Checking right side
                    or (x + ship_size - 1 < len(ships_board) and ships_board[y][i+1] != ' ')

                    # Checking bottom right corner
                    or (x + ship_size - 1 < len(ships_board) and y < len(ships_board) - 1 and ships_board[y+1][i+1] != ' ')

                    # Checking bottom side
                    or (y < len(ships_board) - 1 and ships_board[y+1][i] != ' ')

                    # Checking bottom left corner
                    or (x > 0 and y < len(ships_board) - 1 and ships_board[y-1][i-1] != ' ')
                ):
                    return False, None
            return True, [(i, y) for i in range(x, x + ship_size)]
        else:
            for i in range(y, y + ship_size):
                if (
                    # Checking cell
                    ships_board[i][x] != ' '

                    # Checking left side
                    or (x > 0 and ships_board[i][x] != ' ')

                    # Checking top left corner
                    or (x > 0 and y > 0 and y > 0 and ships_board[i-1][x-1] != ' ')

                    # Checking top side
                    or (y > 0 and ships_board[i-1][x] != ' ')

                    # Checking top right corner
                    or (y > 0 and x < len(ships_board) - 1 and ships_board[i-1][x+1] != ' ')

                    # Checking right side
                    or (x < len(ships_board) - 1 and ships_board[i][x+1] != ' ')

                    # Checking bottom right corner
                    or (x < len(ships_board) - 1 and y + ship_size -1 < len(ships_board) - 1 and ships_board[i+1][x+1] != ' ')

                    # Checking bottom side
                    or (y + ship_size - 1 < len(ships_board) - 1 and ships_board[i+1][x] != ' ')

                    # Checking bottom left corner
                    or (x > 0 and y < len(ships_board) - 1 and ships_board[i+1][x-1] != ' ')
                ):
                    return False, None
            return True, [(x, i) for i in range(y, y + ship_size)]

    # Place ships
    def place_ships_on_board(self):
        # Define ship board
        ships_board = self.create_game_board()

        # Define ships list
        ships_list = [
            {'name': 'single masted'},
            {'name': 'two masted'},
            {'name': 'three masted'},
            {'name': 'four masted'},
        ]

        # PLace ships on board
        for ship in ships_list:
            for i in range(self.ships.get(ship['name'], {}).get('quantity')):
                location_found = False
                attempts = 0

                while not location_found and attempts < 100:
                    is_free, coordinates = self.generate_ships_coordinates(ship['name'], ships_board, self.ships.get(ship['name'], {}).get('size'))

                    if is_free:
                        for coordinate in coordinates:
                            x, y = coordinate
                            ships_board[y][x] = 's'
                        location_found = True
                    else:
                        attempts += 1

                if attempts == 100:
                    print(colored("Error: ", "red", attrs=['bold']) + colored("Unable to place all ships on board. Please try again.", "red"))
                    sys.exit()

        # Return board with ships
        return ships_board