# FastAPI Development Project

A RESTful API built with FastAPI, PostgreSQL, and Python.

## Features

- User authentication
- CRUD operations for posts
- PostgreSQL database integration
- RESTful API endpoints

## Prerequisites

- Python 3.7+
- PostgreSQL
- pip

## Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install fastapi psycopg uvicorn
```
4. Configure PostgreSQL:
   - Database name: fastapi
   - Username: postgres
   - Password: Beenco.@123
   - Host: localhost

## Running the Application

1. Start the server:
```bash
uvicorn app.main:app --reload
```
2. Access the API documentation at:
   - http://localhost:8000/docs
   - http://localhost:8000/redoc

## API Endpoints

- `GET /`: Welcome message
- `/users`: User management endpoints
- `/posts`: Post management endpoints
- `/auth`: Authentication endpoints

## Useful Commands

To add alembic to your project you can use
```bash
pip install alembic
```

To create alembic.ini file you can use
```bash
alembic init alembic
```

To add new revision to database you can use
```bash
alembic revision --autogenerate -m "message"
```

If you changed anything in development use the below command first push the changes to github then to production
```bash
git add .
git commit -m "message"
git push remote main
git push heroku main
```

To add heroku to your project you can use
```bash
heroku login
heroku create your-app-name
```

If you update the database use the below command first before pushing the changes to production
```bash
heroku run "alembic upgrade head"
```

To restart the heroku application you can use
```bash
heroku ps:restart
```

To check logs of your application you can use
```bash
heroku logs -t
```

To check the info of you application you can use
```bash
heroku app:info fastapi-development
```

To create a database you can use
```bash
heroku addons:create heroku-postgresql:essential-0 --app fastapi-development
```

To set exports from .env file in ubuntu you can use
```bash
set -o allexport; source /home/saad/.env; set +o allexport
```

Gunicorn processes can be managed using gunicorn or gunicorn[gevent]

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8080
```   


## Project Structure

```
python-api-development/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── routers/
│       ├── posts.py
│       ├── users.py
│       └── auth.py
```
