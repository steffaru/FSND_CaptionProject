import os
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS
from datetime import datetime
from sqlalchemy import func
from models import setup_db, Movie, Actor
from auth.auth import AuthError, requires_auth
from werkzeug.datastructures import ImmutableMultiDict


def create_app(a, b):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE,PATCH,OPTIONS')
        return response
    
    @app.route('/', methods=['GET'])
    def is_alive():
        return jsonify({
            'code': 200,
            'success': True,
            'message': "Ok"
        })
            
    @app.route('/api/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(f):
        code = 200
        try:
            if f is None:
                code = 401
                abort(code)

            movies = Movie.query.all()
            formatted_movies = [movie.format() for movie in movies]
            if len(formatted_movies) == 0:
                code = 404
                abort(404)

            return jsonify({
                'code': 200,
                'success': True,
                'movies': formatted_movies,
                'total_movies': len(formatted_movies)
            })
        except:
            code = 422
            abort(code)

    @app.route('/api/movies/create', methods=['POST'])
    @requires_auth('post:movie')
    def create_movie(f):
        code = 200
        try:
            if f is None:
                code = 401
                abort(code)

            req = request.get_json()
            new_title = req.get('title', None)
            new_release_date = req.get('release_date', None)
            new_release_date = datetime.strptime(new_release_date, '%Y-%m-%d')
            print(new_title)
            if new_title == "":
                code = 422
                abort(code)            

            movie = Movie(
                title=new_title,
                release_date=new_release_date
            )
            movie.insert()
            return jsonify({
                'code': 200,
                'success': True,
                'created': movie.id,
            })
        except:
            code = 422
            abort(code)

    @app.route('/api/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def update_movie(f, movie_id):
        code = 422
        movie = Movie.query.filter_by(id=movie_id).first()
        if movie is None:
            code = 404
            abort(code)
        try:
            if f is None:
                code = 401
                abort(code)
            req = request.get_json()
            new_title = req.get('title', None)
            new_release= req.get('release_date', None)

            if new_title == "":
                code = 422
                abort(code)

            if movie.title is not None:
                movie.title=new_title
            if movie.release_date is not None:
                movie.release_date=new_release
            movie.update()

            return jsonify({
                'code': 200,
                'success': True,
                'movie_id': movie_id,
            })
        except:
            abort(code)

    @app.route('/api/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(f, movie_id):
        if f is None:
            code = 401
            abort(code)

        movie = Movie.query.filter_by(id=movie_id).first()
        if movie is None:
            code = 404
            abort(code)
        try:
            movie.delete()

            return jsonify({
                'code': 200,
                'success': True,
                'movie': movie_id
            })
        except:
            code = 405
            abort(code)

    @app.route('/api/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(f):
        code = 422
        try:
            if f is None:
                code = 401
                abort(code)

            actors = Actor.query.all()
            formatted_actors = [actor.format() for actor in actors]

            if len(formatted_actors) == 0:
                code = 404
                abort(code)

            return jsonify({
                'code': 200,
                'success': True,
                'actors': formatted_actors,
                'total_actors': len(formatted_actors)
            })
        except:
            abort(code)

    @app.route('/api/actors/create', methods=['POST'])
    @requires_auth('post:actor')
    def create_actor(f):
        code = 422
        try:
            if f is None:
                code = 401
                abort(code)

            req = request.get_json()
            new_name = req.get('name', None)
            new_age = req.get('age', None)
            new_gender = req.get('gender', None)

            if new_name == "":
                code = 422
                abort(code)

            actor = Actor(
                name=new_name,
                age=new_age,
                gender=new_gender
            )
            actor.insert()
            return jsonify({
                'code': 200,
                'success': True,
                'actor_id': actor.id,
            })
        except:
            abort(code)

    @app.route('/api/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def update_actor(f, actor_id):
        code = 422
        actor = Actor.query.filter_by(id=actor_id).first()
        if actor is None:
            code = 404
            abort(code)
        try:
            if f is None:
                code = 401
                abort(code)
            req = request.get_json()
            new_name = req.get('name', None)
            new_age = req.get('age', None)
            new_gender = req.get('gender', None)

            if new_name == "":
                code = 422
                abort(code)

            if actor.name is not None:
                actor.name=new_name
            if actor.age is not None:
                actor.age=new_age
            if actor.gender is not None:
                actor.gender=new_gender
            actor.update()

            return jsonify({
                'code': 200,
                'success': True,
                'actor_id': actor_id,
            })
        except:
            abort(code)

    @app.route('/api/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(f, actor_id):
        code = 405
        actor = Actor.query.filter_by(id=actor_id).first()
        if actor is None:
            code = 404
            abort(code)
        try:
            if f is None:
                code = 401
                abort(code)
            actor.delete()
            return jsonify({
                'code': 200,
                'success': True,
                'actor': actor_id
            })
        except:
            abort(code)


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(401)
    def unauthorized_user(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "unauthorized"
        }), 401

    @app.errorhandler(403)
    def forbidden_user(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "Forbidden"
        }), 403

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method Not Allowed"
        }), 405

    #Error AuthError:
    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response
    
    return app
