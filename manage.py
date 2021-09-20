from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from models import db, seed
from app import create_app as app

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

seed()

if __name__ == '__main__':
    manager.run()