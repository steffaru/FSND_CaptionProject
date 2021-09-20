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
            "release_date": "2021-10-01"},
        {
            "release_date": "2017-09-03",
            "title": "The Leisure Seeker"},
        {
            "release_date": "2004-08-07",
            "title": "Eternal Sunshine of the Spotless Mind"},
        {
            "release_date": "2016-01-29",
            "title": "The Fundamentals of Caring"},
        {
            "release_date": "2021-08-03",
            "title": "A Quiet Place Part II"},
        {
            "release_date": "2021-08-30",
            "title": "Cruella"},
        {
            "release_date": "1927-05-06",
            "title": "7th Heaven"},
        { 
            "release_date": "2000-11-22",
            "title": "102 Dalmatians"},
        {
            "release_date": "2000-04-14",
            "title": "28 Days"},
        {
            "release_date": "2000-01-02",
            "title": "Across the Line"},
        {
            "release_date": "2018-10-18",
            "title": "Ocean Eleven"},
        {
            "release_date": "2000-02-01",
            "title": "The Gift"
        }
    ]
    actors = [
        {
            "age": 77,
            "gender": "M",
            "name": "Robert De Niro"},
        {
            "age": 84,
            "gender": "M",
            "name": "Jack Nicholson"},
        {
            "age": 72,
            "gender": "F",
            "name": "Meryl Streep"},
        {
            "age": 65,
            "gender": "M",
            "name": "Tom Hanks"},
        {
            "age": 79,
            "gender": "F",
            "name": "Elizabeth Taylor"},
        {
            "age": 47,
            "gender": "M",
            "name": "Leonardo DiCaprio"},
        {
            "age": 52,
            "gender": "F",
            "name": "Cate Blanchett"},
        {
            "age": 46,
            "gender": "F",
            "name": "Kate Winslet"},
        {
            "age": 56,
            "gender": "F",
            "name": "Viola Davis"},
        {
            "age": 87,
            "gender": "F",
            "name": "Sophia Loren"},
        {
            "age": 65,
            "gender": "F",
            "name": "Diane Keaton"},
        {
            "age": 54,
            "gender": "F",
            "name": "Julia Roberts"},
        {
            "age": 59,
            "gender": "F",
            "name": "Jodie Foster"},
        {
            "age": 84,
            "gender": "M",
            "name": "Morgan Freeman"},
        {
            "age": 76,
            "gender": "F",
            "name": "Helen Mirren"},
        {
            "age": 61,
            "gender": "F",
            "name": "Angela Bassett"},
        {
            "age": 58,
            "gender": "M",
            "name": "Johnny Depp"},
        {
            "age": 33,
            "gender": "M",
            "name": "Michael Ceraaaaaaaaa"
        },
        {
            "age": 44,
            "gender": "M",
            "name": "John Cena"},
        {
            "age": 50,
            "gender": "M",
            "name": "Robbie Williams"},
        {
            "age": 58,
            "gender": "M",
            "name": "Steve Carrell"},
        {
            "age": 41,
            "gender": "F",
            "name": "Scarlet  Johansson"},
        {
            "age": 51,
            "gender": "F",
            "name": "Viola Davis"
        }
    ]
    for item in movies:
        movie = Movie.query.filter_by(title=item['title']).first()
        if movie is None:
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