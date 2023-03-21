import sys
from termcolor import colored
from .modules.game_board import GameBoard
from .modules.game_parameters import GameParameters
from .modules.game_rules import GameRules

class GameLogic:
    def __init__(self):
        self.max_turns = GameParameters().get_max_turns()
        self.game_board_size = GameParameters().get_game_board_size()
        self.col_headers = GameParameters().get_col_headers()
        self.row_headers = GameParameters().get_row_headers()
        self.hits = 0

    # Convert coordinates
    def convert_coordinates(self, coordinates):
        # Check string length
        if (len(coordinates) == 2 or len(coordinates) == 3):
            # Split string 
            x, y = coordinates[0], coordinates[1:]

            # Check if x and y format is valid
            if x in self.col_headers and y in self.row_headers:
                x = ord(x) - ord('A')
                y = int(y) - 1
                return True, x, y
            else:
                return False, None, None
        else:
            return False, None, None

    # Game logic
    def start_game(self):
        # Generate new ships board and player board
        ships_board = GameBoard().place_ships_on_board()
        player_board = GameBoard().create_game_board()

        # Define hits
        hits = self.hits

        # Display general rules
        GameRules().display_general_rules()

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
        GameRules().display_difficulty_level_rules()

        # Get difficulty level from a user
        while True:
            difficulty_level = input('Choose difficulty level (E / M / H):')
            if difficulty_level in ['E', 'M', 'H']:
                if difficulty_level == 'E':
                    turns = self.max_turns.get('easy')
                    break
                elif difficulty_level == 'M':
                    turns = self.max_turns.get('medium')
                    break
                elif difficulty_level == 'H':
                    turns = self.max_turns.get('hard')
                    break
                break
            else:
                print('Invalid input. Insert one character (E or M or H).')

        # Display player board
        print(colored("Let's begin. Here os your board. When you take a shot, we'll mark its position on it.", 'blue'))
        print(player_board)

        # Game loop
        while hits < 20 and turns > 0:
            # Ask user for coordinates
            coordinates = input("Admiral, enter coordinates to shoot (e.g. D2): ")
            is_valid_coordinates, x, y = self.convert_coordinates(coordinates)

            # Check if coordinates are valid
            if is_valid_coordinates == False:
                print(colored("Invalid coordinates. Please try again.", 'red'))
                continue

            # Check if position has already been hit
            if player_board[y][x] != ' ':
                print(colored("Your already shot there. Please try again.", 'red'))
                continue

            # Check if position is a hit or a miss
            if ships_board[y][x] == 's':
                print(colored("HIT! ", 'green', attrs=['bold']) + colored("Excellent work admiral. Opponents are in fear.", 'green'))
                player_board[y][x] = colored('x', 'green')
                hits += 1
            else:
                print(colored("MISS! ", 'yellow', attrs=['bold']) + colored("Maybe next time you'll make it.", 'yellow'))
                player_board[y][x] = 'o'

            # Display player board with updated shot
            print(player_board)

            # Decrease number of turns
            turns -= 1

        # Game over
        if hits == 20:
            print(colored("Congratulations! You sunk all the ships and won the game!", 'green'))
        else:
            print(colored("Sorry, you ran out of turns. Game over.", 'red') + ' All enemy ships:')
            print(ships_board)