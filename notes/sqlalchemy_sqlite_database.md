# SQLAlchemy + SQLite Database

## What we implemented

We replaced fake in-memory database with a real SQLite database using SQLAlchemy.

Before:

courses = []

This was a fake in-memory database:
- data existed only while server was running
- after restart all data was deleted
- no real tables
- no real SQL practice

Now:

SQLite + SQLAlchemy ORM

This gives us:
- real database file
- real database table
- persistent data
- real CRUD logic
- better API testing practice

---

## Project structure

app/
├── database.py
├── models/
│   └── course.py
├── schemas/
│   └── course.py
├── routes/
│   └── course.py
└── main.py

---

## database.py

database.py is responsible for database connection setup.

Main parts:

- DATABASE_URL
- engine
- SessionLocal
- Base

### DATABASE_URL

sqlite:///./mini_lms.db

This means:

Create and use SQLite database file named mini_lms.db in the project root.

### engine

engine is the database connection object.

It tells SQLAlchemy where the database is located.

### SessionLocal

SessionLocal creates database sessions.

A database session is used to:
- read data
- create data
- update data
- delete data
- commit changes

### Base

Base is used as a parent class for all SQLAlchemy models.

Every database model inherits from Base.

---

## models/course.py

models/course.py describes the real database table.

Course is a SQLAlchemy model, not a Pydantic schema.

### Important difference

schemas/course.py = API request / response validation

models/course.py = database table structure

routes/course.py = API endpoints and business logic

---

## Course model

The Course model creates the courses table.

Fields:

id:
- integer
- primary key
- index

title:
- string
- required
- cannot be null

description:
- string
- optional
- can be null

is_active:
- boolean
- default value is True

---

## main.py

In main.py we imported:

from app.database import engine, Base
from app.models.course import Course

Then we added:

Base.metadata.create_all(bind=engine)

This line creates database tables based on SQLAlchemy models.

Important:

from app.models.course import Course

may look unused, but it is needed so SQLAlchemy knows about the Course model before creating tables.

---

## Result

After running:

uvicorn app.main:app --reload

a new file appeared:

mini_lms.db

This is the real SQLite database file.

The server started successfully and Swagger opened correctly.

---

## Current status

Database connection is ready.

Course SQLAlchemy model is ready.

SQLite database file was created.

Next step:

Rewrite app/routes/course.py from fake in-memory database to real SQLAlchemy CRUD.