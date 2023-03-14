import json, sys
import termcolor as colored
from beautifultable import BeautifulTable as table

# TODO: Display rules

# TODO: Check if user is ready

# Define game parameters
try:
    with open('./data/gameRules.json', 'r') as f:
        gameRules = json.load(f)
        colHeaders = gameRules.get('headers', {}).get('columns', [])
        rowHeaders = gameRules.get('headers', {}).get('rows', [])
        shipNumb = gameRules.get('shipNumb', {})
except FileNotFoundError:
    print(colored('Error: ', 'red', attrs=['bold']) + colored('File not found. ', 'red') + 'Please make sure the `boardHeaders.json` file exists.')
    sys.exit()
except json.JSONDecodeError:
    print(colored('Error: ', 'red', attrs=['bold']) + colored('JSON decoding error. ', 'red') + 'Please check the data in the `boardHeaders.json` file.')
    sys.exit()

gameBoardSize = 10

# Create empty game board
def createGameBoard(gameBoardSize, colHeaders, rowHeaders):
    # Create table
    gameBoard = table()

    # Create headers
    gameBoard.columns.header = colHeaders
    gameBoard.rows.header = rowHeaders
    
    # Create board
    for i in range(gameBoardSize):
        gameBoard.rows[i] = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    
    print(gameBoard)

createGameBoard(gameBoardSize, colHeaders, rowHeaders)

# TODO: Place ships