from flask import Flask
from app.views.views import page


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True,
                template_folder='../app/templates',
                static_folder='../app/static')
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    app.register_blueprint(page)

    return app
