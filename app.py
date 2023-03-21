import warnings
from logic import GameLogic

# Ignore warnings
warnings.filterwarnings("ignore", message="'BeautifulTable.__getitem__' has been deprecated")
warnings.filterwarnings("ignore", message="'BeautifulTable.__len__' has been deprecated")

if __name__ == "__main__":
    GameLogic().start_game()