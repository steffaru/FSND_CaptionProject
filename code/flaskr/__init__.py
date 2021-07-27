import os
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS
from datetime import datetime
from sqlalchemy import func
from models import setup_db, Movie, Actor


def create_app():
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE,OPTIONS')
        return response
    
    @app.route('/movies', methods=['GET'])
    def get_movies():
        movies = Movie.query.all()
        formatted_movies = [movie.format() for movie in movies]

        return jsonify({
            'success': True,
            'movies': formatted_movies,
            'total_movies': len(formatted_movies)

        })

    @app.route('/movies/create', methods=['POST'])
    def create_movie():
        req = request.get_json()
        
        new_title = req.get('title', None)
        new_release_date = req.get('release_date', None)
        new_release_date = datetime.strptime(new_release_date, '%Y-%m-%d')
        movie = Movie(
            title=new_title,
            release_date=new_release_date
        )
        movie.insert()
        return jsonify({
            'success': True,
            'created': movie.id,
        })
    
    @app.route('/actors', methods=['GET'])
    def get_actors():
        actors = Actor.query.all()
        formatted_actors = [actor.format() for actor in actors]

        return jsonify({
            'success': True,
            'actors': formatted_actors,
            'total_actors': len(formatted_actors)

        })

    @app.route('/actors/create', methods=['POST'])
    def create_actor():
        req = request.get_json()
        
        new_name = req.get('name', None)
        new_age = req.get('age', None)
        new_gender = req.get('gender', None)

        actor = Actor(
            name=new_name,
            age=new_age,
            gender=new_gender
        )
        actor.insert()
        return jsonify({
            'success': True,
            'created': actor.id,
        })

    return app
