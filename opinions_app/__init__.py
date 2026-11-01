from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'SECRET KEY'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import cli_commands, error_handlers, forms, models, views

if __name__ == '__main__':
    app.run()