from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'hogehoge'

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
