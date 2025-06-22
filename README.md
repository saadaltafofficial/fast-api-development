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
