from flask import Blueprint, render_template, redirect, url_for

views = Blueprint(__name__, "views")

siteName = "Battleship Game"

# Routes

@views.route("/", endpoint='home')
def home():
    return render_template("home.html", siteName=siteName, subPageName='Home')

@views.route("/game", endpoint='game')
def battleshipGame():
    return render_template("game.html", siteName=siteName, subPageName='Game')