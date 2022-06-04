from flask import Flask
from .config import Config
from .routes import routes

class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_object(Config)


    def register_blueprints(self):
        self.app.register_blueprint(routes)


    def run(self):
        self.register_blueprints()
        self.app.run(debug=True)