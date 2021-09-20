# Capstone Project Full Stack Nanodegree 🎭🎬🎥🤡🐱‍🏍

This project is a **Capstone Project** that I do myself for **Udacity**. In this project you can see movies and actors. If you are director or manager access to much actions; like get, edit, delete and create movies and actors according your asigned rol. As part of the Fullstack Nanodegree, this is a final projetc for ** Full Stack Web Developer Nanodegree Program**. In this project, I applied API endpoint structuring, implementation, Authentication with AUTH0, based on role access management strategies to control different types of user. The last, but not least deploying server with Heroku.

  
  

## Getting Started 🚄

  

### Installing Dependencies ⚙⚙🔩🔩

  

#### Python 3.7 🐍

  

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

  

#### Virtual Enviornment 🦾🦿

  

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

  

#### PIP Dependencies 🧩🧩

  

Once you have your virtual environment setup and running, install dependencies by naviging to the `/code` directory and running:

  

pip install -r requirements.txt

  

This will install all of the required packages we selected within the `requirements.txt` file.

  

##### Key Dependencies 🔑🔑

  

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

  

## Running the server 🧗‍♀️

  

From within the `./flaskr` directory first ensure you are working using your created virtual environment.

  

Each time you open a new terminal session, run:

  

export FLASK_APP=api.py;

  

To run the server, execute:

  

flask run --reload

  

The `--reload` flag will detect file changes and restart the server automatically.

  

## Tasks ⛏⛏

  

### Setup Auth0 🧰🧰

  

1. Create two new Auth0 Account 👩‍💻

2. Select a unique tenant domain

3. Create a new, single page web application

4. Create a new API

- in API Settings:

- Enable RBAC

- Enable Add Permissions in the Access Token

5. Create new API permissions:

- `get:movies`

- `get:actors`

- `post:movie`

- `post:actor`

- `patch:movie`

- `patch:actor`

- `delete:movie`

- `delete:actor`

7. Create new roles for:

- Director

- can `get:actors, get:movies`

- account `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InRQVVJiUEVPYTBVZWt4YmE0MVhjayJ9.eyJpc3MiOiJodHRwczovL2Rldi11ZGFjaXR5LWNhcHN0b25lMjAyMS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEwMjBmNDc4ZTMxZDUwMDY5ZjYyZWM4IiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwL2FwaSIsImlhdCI6MTYzMjEwMzE0MiwiZXhwIjoxNjMyMTg5NTQyLCJhenAiOiJTZWxNZ3U5RUdWRVBjNzZCdW9DaWZ1cklkOGxkendFQiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.a_dJ0oOrFoHgjcqN-NF-K5Tlu20WA7UfVd-guQgVzFNfWczi4SGIDrYWpuhVtSWi4MIKJ9O1LSIr8Frtom5-stLpnF5Qw1_J5ciYwtgInzjOmpNyzRQoKqkSPKzPvecdu80h3la_1NPkBX1NjvHxmUSxfHFSFUJ8P-QRzKykyg83He5Xor89E4y6JPYPVZ_czAaDg2t6TkbJc5zMFZQLBbt9zD2puapqwGhnVqxGJC6D2ablKSfoxHm6lAWtD-X2LBLJe4G7pko6_Pfd63Ykdqw_GsD7AOXCtf6RV3C1NNjRXRl2-8Ch15FqWWdkE-RGnkdR8XIXRqyHXTUwgDy9Kg`

- Manager

- can perform all actions

- account `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InRQVVJiUEVPYTBVZWt4YmE0MVhjayJ9.eyJpc3MiOiJodHRwczovL2Rldi11ZGFjaXR5LWNhcHN0b25lMjAyMS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEwMjBlMzZjNjFmZDcwMDc3ZDA1OWEzIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwL2FwaSIsImlhdCI6MTYzMjA5NDA4NSwiZXhwIjoxNjMyMTgwNDg1LCJhenAiOiJTZWxNZ3U5RUdWRVBjNzZCdW9DaWZ1cklkOGxkendFQiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiXX0.f1nyea5QX9TB9Wtk1uJVW2d7X0ZsYTKZTBCmUKPR6oM03IBjua8h-lSt0m8u5kXqLYXmyO8Gsrxrm_2oWGr1QlXvJXy5dLpvfVnv3Q_Kp0gWMqnwvsoEWt76kP1SAPsa84WpdhrBHxzinL5wkMutlZJzX7ygq_qNG6x_PKB4y6zDVTbfbldltCEHUJr-GOObh_vA8C4ciWW8nrIPF0Dvujll3_dXDo6jugEzBblbWfuygHbUU2qoEfMAiExtMLHcDOlonYEVuC1fRT2XJ8Axo4BTvh1j7nQU1VzTgqTgB-Hz1sXkozJIXRLnVhxgrT2VQrqoKk6_Z7o0iwxcpUyKZA`

8. Test your endpoints with [Postman](https://getpostman.com/).🧫🧫

- Register 2 users - assign the Director role to one and Manager role to the other.

- Sign into each account and make note of the JWT.

- Import the postman collection `capstone.postman_collection.json`

- Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).

- Run the collection and correct any errors.

- Export the collection overwriting the one we've included so that we have your proper JWTs during review!

   

# APIS 

## GET🥙

	> Movies 🐱‍🐉= https://capstone-project-steffaru.herokuapp.com/api/movies 
	> Actors 🧝‍♂️= https://capstone-project-steffaru.herokuapp.com/api/actors

    {
	    "code": 200,
	    "movies": [
		    {				    
				"id": 1,
				"release_date": "Fri, 01 Oct 1999 00:00:00 GMT",
				"title": "Hellfish"
			}, 
		    {
			    "id": 2,
			    "release_date": "Thu, 01 Oct 1992 00:00:00 GMT",
			    "title": "Batman Returns"
		    }
	    ],
	    "success": true,
	    "total_movies": number random
	}
	
    {
	    "actors": [
		    {
				"age": 77,
				"gender": "M",
				"id": 1,
				"name": "Robert De Niro"},
		    {
			    "age": 84,
			    "gender": "M",
			    "id": 2,
			    "name": "Jack Nicholson"},
	    ],
	    "code": 200,
	    "success": true,
	    "total_actors": random number
    }


> 

## POST 🍜

>
> **Movies** 				

    curl -d '{"title":"value1", "release_date":"value2"}' -H "Content-Type: application/json" -X POST https://capstone-project-steffaru.herokuapp.com/api/movies/create

> Return
	
	    {
		     "code" :  200,
		     "success":  True,
		     "created": movie.id
	    }

> 
> 
> **Actors** 
    

    curl -d '{"name":"value1", "age":"value2", "gender": "value3"}' -H "Content-Type: application/json" -X POST https://capstone-project-steffaru.herokuapp.com/api/actors/create

> Return

    {
    	 "code" :  200,
    	 "success":  True,
    	 "created": actor.id
    }


## PATCH 🥂


> **Movies** 				

    curl -d '{"title":"value1", "release_date":"value2"}' -H "Content-Type: application/json" -X PATCH https://capstone-project-steffaru.herokuapp.com/api/movies/12

> Return
	
	    {
		     "code" :  200,
		     "movie_id": 12,
		     "success": True
	    }

> 
> 
> **Actors** 
    

    curl -d '{"name":"value1", "age":"value2", "gender": "value3"}' -H "Content-Type: application/json" -X PATCH https://capstone-project-steffaru.herokuapp.com/api/actors/4

> Return

    {
    	 "code" :  200,
    	 "actor_id":  4,
    	 "success": True
    }

## DELETE 🍄


> **Movies** 				

    curl -X  DELETE https://capstone-project-steffaru.herokuapp.com/api/movies/12

> Return
	
	    {
		     "code" :  200,
		     "movie_id": 12,
		     "success": True
	    }

> 
> 
> **Actors** 
    

    curl -X  DELETE https://capstone-project-steffaru.herokuapp.com/api/actors/4

> Return

    {
    	 "code" :  200,
    	 "actor_id":  4,
    	 "success": True
    }




> ***ENJOY***
