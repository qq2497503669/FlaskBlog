from flask import Flask
from config import Config
app = Flask(__name__, static_url_path="/static",
            static_folder="../static",
            template_folder="../templates",
            )

app.config.from_object(Config)

from app import routes

if __name__ == '__main__':
    print('Hello world')
