from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from models import db, Movie, Actor
from app import create_app as app

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

def seed():
    movies = [
        {
            "title":"Hellfish",
            "release_date": "1999-10-01"},
        {
            "title":"Batman Returns",
            "release_date": "1992-10-01"},
        {
            "title":"Spiderman",
            "release_date": "2015-10-01"},
        {
            "title":"Thor Ragnarok",
            "release_date": "2017-10-01"},
        {
            "title":"Guardianes de la Galaxia",
            "release_date": "2019-10-01"},
        {
            "title":"Scarlet Witch",
            "release_date": "2021-10-01"
        }
    ]
    for item in movies:
        movie = Movie(
                title=item.title,
                release_date=item.release_date
            )
        movie.insert()    
    
if __name__ == '__main__':
    manager.run()