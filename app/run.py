from flask import Flask
from app.views import page


def bootstrap():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py')

    app.register_blueprint(page)

    return app
