from flask import Flask
from routes.__init__ import api


application = Flask(__name__)
application.register_blueprint(api)


if __name__ == '__main__':
    application.run()