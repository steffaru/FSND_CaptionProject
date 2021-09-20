import os
from sqlalchemy import Column, String, Integer, Date
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

database_path = os.getenv('DATABASE_URL')

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    migrate = Migrate(app, db)


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
                title=item['title'],
                release_date=item['release_date']
            )
        movie.insert()    

'''
Movie

'''
class Movie(db.Model):  
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_date = Column(Date)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }

'''
Actor

'''
class Actor(db.Model):  
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }