from flask import Flask

app = Flask(__name__, static_url_path="/static",
            static_folder="../static",
            template_folder="../templates",
            )

from app import routes

if __name__ == '__main__':
    print('Hello world')
