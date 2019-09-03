import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# Globally accessible libraries
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app(test_config=None):
    """Initialising the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialising the plugins
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # registering blueprints
    from feedback.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
