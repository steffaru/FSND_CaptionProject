import os
import unittest
import json
from functools import wraps
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor


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
        self.header = {'Content-Type': 'application/json', 'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InRQVVJiUEVPYTBVZWt4YmE0MVhjayJ9.eyJpc3MiOiJodHRwczovL2Rldi11ZGFjaXR5LWNhcHN0b25lMjAyMS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEwMjBlMzZjNjFmZDcwMDc3ZDA1OWEzIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwL2FwaSIsImlhdCI6MTYzMDIwMTUyMCwiZXhwIjoxNjMwMjg3OTIwLCJhenAiOiJTZWxNZ3U5RUdWRVBjNzZCdW9DaWZ1cklkOGxkendFQiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiXX0.NncE9PLAGT1t0hvoZTKqeKqEYwe8SgbV-5KN-D61CNMMt4k16Dkw-nVi_0V0VzxnI3dFgRzNFZ-XnbFeej_lV583pGURGYjr8n362NI7AeumnC8ONO7na0rAgSzx-IrQ-eE9ANcNjcvOCBq_S2e6KBHbDNJLQ19kC9AhHOA6QmVzg_fmyDUkWOiVybOzaj6Zn2UaDnviRYRINWaL_jR-_PqrNCP3k6XcxA5p38y73tXAqj2TWHqGw99oQLyRBrPH2n8PQc5HC3HSFn-ZEPJUYhK0gOnBApTqADVstGSrahkgKG3pVDiyI2hE2FSxB0h4jfxNAgUmcuweeJ8_ajVyhQ"}

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
    def test_get_movies(self):
        res = self.client().get('http://localhost:5000/api/movies', headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))
        self.assertTrue(data['total_movies'])

    def test_404_if_movies_doesnt_exist(self):
        res = self.client().get('http://localhost:5000/api/moviss', headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # #POST MOVIE
    def test_post_new_movie(self):
        res = self.client().post(
            'http://localhost:5000/api/movies/create',
            json={
                'title': 'Ocean Eyes',
                'release_date': '2018-10-01'
                },
            headers=self.header)
        movies = Movie.query.all()
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(movies))
    
    def test_422_if_new_movie_is_unprocessable(self):
        res = self.client().post(
            'http://localhost:5000/api/movies/create',
            json={'title': ""},
            headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    #DELETE MOVIES
    def test_delete_movie(self):
        res = self.client().delete('http://localhost:5000/api/movies/43', headers=self.header)
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 43).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movie, None)

    def test_404_if_movie_delete_doesnt_exist(self):
        res = self.client().delete('http://localhost:5000/api/movies/1000', headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    #PATCH MOVIES
    def test_patch_movie(self):  
        res = self.client().patch(
            'http://localhost:5000/api/movies/11',
            json={
                'title': 'The Gifteddddddddddddddd',
                'release_date': '2000-02-01'
                },
            headers=self.header)
        movies = Movie.query.all()
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(movies))

    def test_404_if_movie_patch_doesnt_exist(self):
        res = self.client().patch(
            'http://localhost:5000/api/movies/8000',
            json={
                'title': '',
                'release_date':''
                },
            headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_422_if_patch_movie_is_unprocessable(self):
        res = self.client().patch(
            'http://localhost:5000/api/movies/6',
            json={'title': ""},
            headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # #GET ACTORS
    def test_get_actors(self):
        res = self.client().get('/api/actors', headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))
        self.assertTrue(data['total_actors'])

    def test_404_if_actors_doesnt_exist(self):
        res = self.client().get('http://localhost:5000/api/actores', headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # #POST ACTOR
    def test_post_new_actor(self):
        res = self.client().post(
            'http://localhost:5000/api/actors/create',
            json={
                'name': 'Viola Davis',
                'age': 51,
                'gender': 'F'
                },
            headers=self.header)
        actors = Movie.query.all()
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(actors))
    
    def test_422_if_new_actor_is_unprocessable(self):
        res = self.client().post(
            'http://localhost:5000/api/actors/create',
            json={},
            headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    #DELETE ACTOR
    def test_delete_actor(self):
        res = self.client().delete('http://localhost:5000/api/actors/88', headers=self.header)
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 88).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actor, None)

    def test_404_if_actor_delete_doesnt_exist(self):
        res = self.client().delete('http://localhost:5000/api/actors/10000', headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    #PATCH ACTOR
    def test_patch_actor(self):  
        res = self.client().patch(
            'http://localhost:5000/api/actors/19',
            json={
                'name': 'Steve Carrell',
                'age': 58,
                'gender': 'M'
                },
            headers=self.header)
        actors = Actor.query.all()
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(actors))

    def test_404_if_actor_patch_doesnt_exist(self):
        res = self.client().patch(
            'http://localhost:5000/api/actors/8000',
            json={
                'name': 'pepe grillo',
                'age': '',
                'gender': ''
                },
            headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_422_if_patch_actor_is_unprocessable(self):
        res = self.client().patch(
            'http://localhost:5000/api/actors/8',
            json={},
            headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
