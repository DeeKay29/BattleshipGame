from flask import Flask
from termcolor import colored

from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")

if __name__ == "__main__":
    try:
        app.run(debug=True, port=8000)
    except Exception as e:
        print(colored(f'An error occurred: {e}', 'red'))