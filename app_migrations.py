from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from db_create import db_name

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:252601993@localhost/'+db_name
db = SQLAlchemy(app)


migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)


class User(db.Model):
    name = db.Column(db.String(255), primary_key=True)
    favcolor = db.Column(db.String(255), unique=False)
    pet = db.Column(db.String(255), unique=False)

    def __init__(self, name, favcolor, pet ):
        self.name = name
        self.favcolor = favcolor
        self.pet = pet



if __name__ == '__main__':
    manager.run()
