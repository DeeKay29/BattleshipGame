from flask import Blueprint, render_template
from logic.board import Board

views = Blueprint(__name__, "views")

siteName = "Battleship Game"

# Routes

@views.route("/", endpoint='home')
def home():
    return render_template("home.html", siteName=siteName, subPageName='Home')

@views.route("/game", endpoint='game')
def battleshipGame():
    game_board = Board()
    return render_template("game.html", siteName=siteName, subPageName='Game', board=game_board.board, headers=game_board.headers, board_size=game_board.board_size)