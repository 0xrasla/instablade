from flask import Flask
from .config import Config
from .routes import routes
from flask_bootstrap import Bootstrap
class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_object(Config)
        self.app.config.setdefault("BOOTSTRAP_USE_MINIFIED", True)
        self.app.config.setdefault("BOOTSTRAP_SERVE_LOCAL", True)

    def register_blueprints(self):
        self.app.register_blueprint(routes)


    def run(self):
        self.register_blueprints()
        Bootstrap(self.app)
        self.app.run(debug=True)