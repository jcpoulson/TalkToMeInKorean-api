from flask import Flask
from routes.__init__ import api


app = Flask(__name__)
app.register_blueprint(api)


if __name__ == '__main__':
    app.run(debug=True, port=5000)