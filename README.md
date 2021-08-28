# Capstone Project Full Stack Nanodegree  🎭🎬🎥🤡🐱‍🏍
This project is a **Capstone Project** that I do myself for **Udacity**. In this project you can see movies and actors. If you are director or manager access to much actions; like get, edit, delete and create movies and actors according your asigned rol. As part of the Fullstack Nanodegree, this is a final projetc for ** Full Stack Web Developer Nanodegree Program**. In this project, I applied API endpoint structuring, implementation, Authentication with AUTH0, based on role access management strategies to control different types of user. The last, but not least deploying server with Heroku.


## Getting Started  🚄

### Installing Dependencies  ⚙⚙🔩🔩

#### Python 3.7  🐍

Follow instructions to install the latest version of python for your platform in the  [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment  🦾🦿

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the  [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies  🧩🧩

Once you have your virtual environment setup and running, install dependencies by naviging to the  `/code`  directory and running:

pip install -r requirements.txt

This will install all of the required packages we selected within the  `requirements.txt`  file.

##### Key Dependencies  🔑🔑

-   [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.
    
-   [SQLAlchemy](https://www.sqlalchemy.org/)  and  [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)  are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in  `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.
    
-   [jose](https://python-jose.readthedocs.io/en/latest/)  JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.
    

## Running the server  🧗‍♀️

From within the  `./flaskr`  directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

export FLASK_APP=api.py;

To run the server, execute:

flask run --reload

The  `--reload`  flag will detect file changes and restart the server automatically.

## Tasks  ⛏⛏

### Setup Auth0  🧰🧰

1.  Create two new Auth0 Account  👩‍💻
    
2.  Select a unique tenant domain
    
3.  Create a new, single page web application
    
4.  Create a new API
    
    -   in API Settings:
        -   Enable RBAC
        -   Enable Add Permissions in the Access Token
5.  Create new API permissions:
    
    -   `get:movies`
    -   `get:actors`
    -   `post:movie`
    -   `post:actor`
    -   `patch:movie`
    -   `patch:actor`
    -   `delete:movie`
    -   `delete:actor`
7.  Create new roles for:
    
    -   Director
        -   can  `get:actors, get:movies`
            
        -   account  `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InRQVVJiUEVPYTBVZWt4YmE0MVhjayJ9.eyJpc3MiOiJodHRwczovL2Rldi11ZGFjaXR5LWNhcHN0b25lMjAyMS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEwMjBmNDc4ZTMxZDUwMDY5ZjYyZWM4IiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwL2FwaSIsImlhdCI6MTYzMDExMTk1OSwiZXhwIjoxNjMwMTk4MzU5LCJhenAiOiJTZWxNZ3U5RUdWRVBjNzZCdW9DaWZ1cklkOGxkendFQiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.XGWOWeDWaZ4c7FtiGVXoeYhzjvDDV4cJtTNJC6z7VEge81nHvGLoNGRsV72Y2H4u7PGjwLg2Sk9tvR4u8vmbGLIbKU9dbpgorwD8IbAOH99UPtcOgujBc803yoiP6qbg5NBLtCyDZbNxiOpfXXtlGLCwRAcIIq0VCUkOocPvBEauCr8PYjlgXA4s3VJ9vD0_GLBlIMf12THN5HRgcklo-Ab0NydjzVKKs8X9WIYspj4ClImF9QU9thI6f53thg7KN-lq3eg0AVb5_Xbb1hU2dFdxHe1nj4nKnA36Iq1qfg90H940yIO5Zzjr4uy8bbTJtV0P53mGdNnZBEBKyPtrKQ`
            
        -   Manager
            
        -   can perform all actions
            
        -   account  `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InRQVVJiUEVPYTBVZWt4YmE0MVhjayJ9.eyJpc3MiOiJodHRwczovL2Rldi11ZGFjaXR5LWNhcHN0b25lMjAyMS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEwMjBlMzZjNjFmZDcwMDc3ZDA1OWEzIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwL2FwaSIsImlhdCI6MTYzMDEwNjg3OSwiZXhwIjoxNjMwMTkzMjc5LCJhenAiOiJTZWxNZ3U5RUdWRVBjNzZCdW9DaWZ1cklkOGxkendFQiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiXX0.mO9TEjhZCTZ_BOFFT2q-td8f4JUEI22QiM-Izo2LK-l5wuFNQ8SZgJIsmBl2xTCH7yPWjV2QFrjAkyX49GN3yyO6ciBTZPKUg5LLYEgJR5xMZjWLLdT0S1NBH1OOe0BzqxfDtxUxcajcjXiNbwkxUIJ6gE-vOue0n1n7BSqAqKxryge-UYMy9Ez5kjGm3VOrmOOH0bRsvq7jBNC8WqlPgoMVpsCdyNMgNpgEgQ86EYCiLLWZ4Ctst5yXlj2xgFBqJlJiXx1vUMgvfBUFGf2ukMd068RL6U5PG2AfBrsfepr74CcmA2eFAeCsaeWoSPiA-sKXmpyvlKkv1wCDmlLODg`
            
8.  Test your endpoints with  [Postman](https://getpostman.com/).🧫🧫
    
    -   Register 2 users - assign the Director role to one and Manager role to the other.
    -   Sign into each account and make note of the JWT.
    -   Import the postman collection  `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
    -   Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
    -   Run the collection and correct any errors.
    -   Export the collection overwriting the one we've included so that we have your proper JWTs during review!

### Implement The Server  ♀️🤹‍

1.  `./code/auth/auth.py`
2.  `./code/flaskr/api.py`

