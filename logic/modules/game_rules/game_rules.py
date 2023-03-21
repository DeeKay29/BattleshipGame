import json
import sys
from termcolor import colored

class GameRules:
    def __init__(self, filepath='./data/gameRules.json'):
        self.filepath = filepath
        try:
            with open('./data/game_data/gameRules.json', 'r') as f:
                self.game_rules = json.load(f)
        except FileNotFoundError:
            print(colored('Error: ', 'red', attrs=['bold']) + colored('File not found. ', 'red') + 'Please make sure the `gameRules.json` file exists.')
            sys.exit()
        except json.JSONDecodeError:
            print(colored('Error: ', 'red', attrs=['bold']) + colored('JSON decoding error. ', 'red') + 'Please check the data in the `gameRules.json` file.')
            sys.exit()

    # Display general rules
    def display_general_rules(self):
        for rule in self.game_rules['general rules']:
            print(colored(rule, 'blue'))
    
    #Display difficulty level rules
    def display_difficulty_level_rules(self):
        for rule in self.game_rules['difficulty level rules']:
            print(colored(rule, 'blue'))