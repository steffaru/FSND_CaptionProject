import os
import unittest
import json
from functools import wraps
from flask_sqlalchemy import SQLAlchemy

from flaskr.api import create_app
from db.models import setup_db, Movie, Actor


class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone1"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'postgres',
            '123456',
            'localhost:5432',
            self.database_name)
        setup_db(self.app)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    #GET MOVIES
    # def test_get_movies(self):
    #     res = self.client().get('/api/movies')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(data['movies']))
    #     self.assertTrue(data['total_movies'])

    # def test_404_if_movies_doesnt_exist(self):
    #     res = self.client().get('http://localhost:5000/api/movies')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')

    # #POST MOVIE
    # def test_post_new_movie(self):
    #     res = self.client().post(
    #         'http://localhost:5000/api/movies/create',
    #         json={
    #             'title': 'The Married',
    #             'release_date': '2018-10-01'
    #             },
    #         headers={'Content-Type': 'application/json'})
    #     movies = Movie.query.all()
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(movies))
    
    # def test_422_if_new_movie_is_unprocessable(self):
    #     res = self.client().post(
    #         'http://localhost:5000/api/movies/create',
    #         json={},
    #         headers={'Content-Type': 'application/json'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unprocessable')

    # #DELETE MOVIES
    # def test_delete_movie(self):
    #     res = self.client().delete('http://localhost:5000/api/movies/15')
    #     data = json.loads(res.data)

    #     movie = Movie.query.filter(Movie.id == 15).one_or_none()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(movie, None)

    # def test_404_if_movie_delete_doesnt_exist(self):
    #     res = self.client().delete('http://localhost:5000/api/movies/1000')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')

    # #PATCH MOVIES
    # def test_patch_movie(self):  
    #     res = self.client().patch(
    #         'http://localhost:5000/api/movies/10',
    #         json={
    #             'title': 'The Engagement is bad',
    #             'release_date': '2021-01-01'
    #             },
    #         headers={'Content-Type': 'application/json'})
    #     movies = Movie.query.all()
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(movies))

    def test_404_if_movie_patch_doesnt_exist(self):
        res = self.client().patch(
            'http://localhost:5000/api/movies/8000',
            json={
                'title': '',
                'release_date':''
                },
            headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_422_if_patch_movie_is_unprocessable(self):
        res = self.client().patch(
            'http://localhost:5000/api/movies/8',
            json={},
            headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # #GET ACTORS
    # def test_get_actors(self):
    #     res = self.client().get('/api/actors')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(data['actors']))
    #     self.assertTrue(data['total_actors'])

    # def test_404_if_actors_doesnt_exist(self):
    #     res = self.client().get('http://localhost:5000/api/actors')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')

    # #POST ACTOR
    # def test_post_new_actor(self):
    #     res = self.client().post(
    #         'http://localhost:5000/api/actors/create',
    #         json={
    #             'name': 'John Cena',
    #             'age': 44,
    #             'gender': 'M'
    #             },
    #         headers={'Content-Type': 'application/json'})
    #     actors = Movie.query.all()
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(actors))
    
    # def test_422_if_new_actor_is_unprocessable(self):
    #     res = self.client().post(
    #         'http://localhost:5000/api/actors/create',
    #         json={},
    #         headers={'Content-Type': 'application/json'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unprocessable')

    # #DELETE ACTOR
    # def test_delete_actor(self):
    #     res = self.client().delete('http://localhost:5000/api/actors/15')
    #     data = json.loads(res.data)

    #     actor = Actor.query.filter(Actor.id == 1).one_or_none()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(actor, None)

    # def test_404_if_actor_delete_doesnt_exist(self):
    #     res = self.client().delete('http://localhost:5000/api/actors/10000')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')

    # #PATCH ACTOR
    # def test_patch_actor(self):  
    #     res = self.client().patch(
    #         'http://localhost:5000/api/actors/28',
    #         json={
    #             'name': 'Michael Cera or Cena',
    #             'age': 33,
    #             'gender': 'M'
    #             },
    #         headers={'Content-Type': 'application/json'})
    #     actors = Actor.query.all()
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(actors))

    # def test_404_if_actor_patch_doesnt_exist(self):
    #     res = self.client().patch(
    #         'http://localhost:5000/api/actors/8000',
    #         json={
    #             'name': 'pepe grillo',
    #             'age': '',
    #             'gender': ''
    #             },
    #         headers={'Content-Type': 'application/json'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')

    # def test_422_if_patch_actor_is_unprocessable(self):
    #     res = self.client().patch(
    #         'http://localhost:5000/api/actors/8',
    #         json={},
    #         headers={'Content-Type': 'application/json'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unprocessable')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
