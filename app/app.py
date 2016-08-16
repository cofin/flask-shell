from flask import Flask


def bootstrap():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py')

    @app.route('/')
    def index():
        """
        Render a Hello World response.

        :return: Flask response
        """
        return app.config['HELLO']

    return app
