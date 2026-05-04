# Mini LMS API

Mini LMS API is a practice project created to improve QA skills in backend testing, API validation, and automation preparation.

This project is focused not only on writing endpoints, but also on understanding how backend systems work and how QA engineers test them in real projects.

---

# Project Goals

This project helps practice:

* FastAPI fundamentals
* request / response validation
* routes and routers
* Swagger / OpenAPI documentation
* Postman API testing
* CRUD operations
* fake database logic before real DB integration
* API automation preparation with pytest + requests
* GitHub portfolio structure for QA interviews

---

# Tech Stack

* Python
* FastAPI
* Pydantic
* Swagger UI / OpenAPI
* Postman
* SQLAlchemy (planned)
* SQLite / PostgreSQL (planned)
* Pytest (planned)
* Requests (planned)

---

# Current Features

Implemented:

* project structure setup
* FastAPI app initialization
* health check endpoint
* full CRUD for /courses
* request body validation using Pydantic schemas
* automatic Swagger documentation
* fake in-memory database
* architecture notes for interview preparation

---

# API Endpoints

## Health Check

GET /health

Used to verify that the API server is running correctly.

---

## Courses CRUD

GET /courses
GET /courses/{course_id}
POST /courses
PUT /courses/{course_id}
DELETE /courses/{course_id}

### POST /courses

Create new course.

* receives request body: title, description, is_active
* validates data using Pydantic schema
* generates fake ID automatically
* saves object into temporary fake database (courses = [])
* returns created object

---

### GET /courses

Get all courses.

* returns full list of created courses

---

### GET /courses/{course_id}

Get single course by ID.

* searches course inside fake database
* returns found course
* returns 404 if course does not exist

---

### PUT /courses/{course_id}

Update course by ID.

* searches existing course
* updates title, description, is_active
* returns updated object
* returns 404 if course does not exist

---

### DELETE /courses/{course_id}

Delete course by ID.

* finds course inside fake database
* removes it from list
* returns success message
* returns 404 if course does not exist

---

# Fake Database Logic

Instead of a real database, the project currently uses:

courses = []

This is a temporary in-memory storage:

* data exists only while server is running
* after restart everything is deleted
* useful for learning API logic before connecting real database

This helps fully understand CRUD behavior before moving to SQLAlchemy and PostgreSQL.

---

# Project Structure

mini-lms-api/

app/
main.py

routes/
└── course.py

schemas/
└── course.py

models/

tests/
└── api/

notes/
├── schemas_and_validation.md
├── routes_and_routers.md
├── swagger_and_postman.md
└── crud_fake_database.md

requirements.txt
.gitignore
README.md

---

# Why This Project Matters for QA

This is not just a coding exercise.

It is a QA-focused backend project created to:

* understand how APIs are built
* improve API testing confidence
* prepare stronger interview answers
* practice real-world backend validation
* build a strong GitHub portfolio project

This helps bridge the gap between Manual QA and Automation QA.

---

# Next Steps

Planned implementation:

* SQLAlchemy models
* SQLite / PostgreSQL integration
* automated API tests
* negative and validation scenarios
* authentication testing
* CI-ready project structure

---

# Interview Value

This project can be used during QA interviews to explain:

* how request validation works
* how Swagger generates JSON automatically
* how Postman testing is performed
* how routes and routers work
* how backend + QA collaboration happens
* how API automation can be structured

It demonstrates both technical understanding and practical testing mindset.