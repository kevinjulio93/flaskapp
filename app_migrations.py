from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/loco'
db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)


class User(db.Model):
    name = db.Column(db.String(255), primary_key=True)
    favcolor = db.Column(db.String(255), unique=False)
    pet = db.Column(db.String(255), unique=False)


if __name__ == '__main__':
    manager.run()
