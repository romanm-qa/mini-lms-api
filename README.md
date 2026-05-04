# Mini LMS API

Mini LMS API is a portfolio-ready backend practice project created to improve QA skills in API testing, backend validation, database understanding, and automation preparation.

This project is focused not only on building endpoints, but also on understanding how real backend systems work and how QA engineers test them in production environments.

The goal is to bridge the gap between Manual QA and Automation QA by combining API testing, backend logic validation, database understanding, and test automation preparation in one real-world style project.

---

# Project Goals

This project helps practice:

* FastAPI fundamentals
* request / response validation
* routes and routers architecture
* Swagger / OpenAPI documentation
* Postman API testing
* CRUD operations
* backend validation logic
* SQLAlchemy fundamentals
* SQLite database integration
* API automation preparation with pytest + requests
* GitHub portfolio structure for QA interviews

---

# Tech Stack

* Python
* FastAPI
* Pydantic
* Swagger UI / OpenAPI
* Postman
* SQLAlchemy
* SQLite
* PostgreSQL (planned)
* Pytest (planned)
* Requests (planned)

---

# Current Features

Implemented:

* project structure setup
* FastAPI app initialization
* health check endpoint
* full CRUD structure for /courses
* request body validation using Pydantic schemas
* automatic Swagger documentation
* SQLAlchemy setup
* SQLite database connection
* database.py configuration
* Course model using SQLAlchemy ORM
* database table creation with Base.metadata.create_all()
* backend architecture notes for interview preparation

The project is intentionally built step by step:
first understanding CRUD logic and API structure, then moving to real database integration using SQLAlchemy and SQLite.

This approach helps better understand how backend systems work internally.

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

At this stage, the API structure is fully prepared, and the project is transitioning from fake in-memory CRUD logic to real database CRUD using SQLAlchemy sessions.

---

## POST /courses

Create a new course.

### Logic

* receives request body: title, description, is_active
* validates data using Pydantic schema
* creates course object
* saves data into database
* returns created object

### Example Request

{
  "title": "FastAPI for QA",
  "description": "Practice course for API testing",
  "is_active": true
}

### Example Response

{
  "id": 1,
  "title": "FastAPI for QA",
  "description": "Practice course for API testing",
  "is_active": true
}

---

## GET /courses

Get all courses.

### Logic

* returns full list of created courses from database

---

## GET /courses/{course_id}

Get a single course by ID.

### Logic

* searches course inside database
* returns found course
* returns 404 if course does not exist

### Example Error Response

{
  "detail": "Course not found"
}

---

## PUT /courses/{course_id}

Update course by ID.

### Logic

* searches existing course
* updates title, description, is_active
* saves updated object
* returns updated object
* returns 404 if course does not exist

---

## DELETE /courses/{course_id}

Delete course by ID.

### Logic

* finds course inside database
* removes it from database
* returns success message
* returns 404 if course does not exist

### Example Response

{
  "message": "Course deleted successfully"
}

---

# Database Architecture

The project now uses real database architecture with:

* SQLAlchemy ORM
* SQLite local database
* engine configuration
* session management
* declarative base models

Current database file:

mini_lms.db

Core database configuration:

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

This allows the project to move from simple fake CRUD logic to production-style backend architecture.

It also helps understand how backend services work in real QA environments.

---

# Project Structure

mini-lms-api/

app/
├── main.py
├── database.py
├── routes/
│   └── course.py
├── schemas/
│   └── course.py
├── models/
│   └── course.py

tests/
└── api/

notes/
├── schemas_and_validation.md
├── routes_and_routers.md
├── swagger_and_postman.md
├── crud_fake_database.md
└── sqlalchemy_sqlite_database.md

mini_lms.db

requirements.txt
.gitignore
README.md

---

# Why This Project Matters for QA

This is not just a coding exercise.

This is a QA-focused backend project created to:

* understand how APIs are built
* improve API testing confidence
* understand backend validation logic
* understand database behavior
* prepare stronger technical interview answers
* practice real-world backend validation
* improve collaboration understanding between QA and developers
* build a strong GitHub portfolio project

This project helps transition from Manual QA mindset to stronger Backend QA / Automation QA thinking.

---

# Next Steps

Planned implementation:

* connect routes to real SQLAlchemy sessions
* full CRUD using database queries
* PostgreSQL support
* automated API tests with pytest
* negative test scenarios
* validation testing
* authentication testing
* API test structure with pytest + requests
* CI-ready project structure

The next major milestone is full CRUD using SQLAlchemy queries instead of temporary fake logic.

This is where the project becomes significantly stronger for QA automation interviews.

---

# Interview Value

This project can be used during QA interviews to explain:

* how request validation works
* how Pydantic schemas work
* how Swagger generates OpenAPI documentation
* how Postman testing is performed
* how routes and routers work
* how backend + QA collaboration happens
* how CRUD operations work internally
* how SQLAlchemy works
* how SQLite differs from fake in-memory storage
* how backend models are created
* how API automation can be structured

This demonstrates both technical understanding and practical testing mindset.

It shows that the candidate understands not only testing, but also how backend systems are designed and validated.