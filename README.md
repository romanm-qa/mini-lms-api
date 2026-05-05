# Mini LMS API

Mini LMS API is a practice project created to improve QA skills in backend testing, API validation, SQL verification, and API automation preparation.

This project is focused not only on writing endpoints, but also on understanding how backend systems work and how QA engineers test real business logic in production systems.

The project simulates a small Learning Management System with users, courses, enrollments, progress tracking, and certificate issuance logic.

---

# Project Goals

This project helps practice:

- FastAPI fundamentals
- request / response validation
- routes and routers
- Swagger / OpenAPI documentation
- Postman API testing
- CRUD operations
- SQLAlchemy ORM
- SQLite database validation
- API business logic testing
- negative scenarios and edge cases
- API automation preparation with pytest + requests
- GitHub portfolio structure for QA interviews

---

# Tech Stack

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Swagger UI / OpenAPI
- Postman
- DB Browser for SQLite
- Pytest planned
- Requests planned

---

# Project Structure

app/
│
├── main.py
│
├── database.py
│
├── models/
│   ├── course.py
│   ├── user.py
│   └── enrollment.py
│
├── schemas/
│   ├── course.py
│   ├── user.py
│   └── enrollment.py
│
└── routes/
    ├── course.py
    ├── users.py
    └── enrollment.py

notes/
├── users_crud_sqlite_business_logic.md
└── enrollments_crud_and_business_logic.md

---

# Entities

## Courses

Stores LMS courses.

Main fields:

- id
- title
- description
- category
- level
- duration_minutes
- price
- is_active

CRUD implemented.

---

## Users

Stores platform users.

Main fields:

- id
- first_name
- last_name
- email
- role
- progress
- certificate
- is_active

CRUD implemented.

Business logic includes progress tracking and certificate validation.

---

## Enrollments

Main business entity.

Connects:

- users
- courses

Tracks:

- which user is enrolled in which course
- progress
- completion status
- certificate issuance
- completion date

Main fields:

- id
- user_id
- course_id
- progress
- status
- certificate_issued
- enrolled_at
- completed_at

Full CRUD implemented.

---

# Business Logic

## Enrollment completion logic

If progress == 100:

System automatically updates:

- status → completed
- certificate_issued → True
- completed_at → current datetime

If progress < 100:

System automatically updates:

- status → in_progress
- certificate_issued → False
- completed_at → NULL

This helps practice real API business rule testing, not only simple CRUD.

---

# API Endpoints

## Courses

- POST /courses
- GET /courses
- GET /courses/{id}
- PUT /courses/{id}
- DELETE /courses/{id}

---

## Users

- POST /users
- GET /users
- GET /users/{id}
- PUT /users/{id}
- PATCH /users/{id}
- DELETE /users/{id}

---

## Enrollments

- POST /enrollments
- GET /enrollments
- GET /enrollments/{id}
- PATCH /enrollments/{id}
- DELETE /enrollments/{id}

---

# Testing Focus

This project is designed not only for development practice, but mainly for QA practice:

- API validation
- required fields testing
- negative testing
- edge cases
- duplicate validation
- business logic validation
- SQL verification
- database state validation
- Swagger vs Postman comparison
- API automation preparation

---

# Next Steps

Planned next improvements:

- API test cases documentation
- Postman collection improvement
- pytest + requests API automation
- SQL JOIN practice
- advanced edge cases
- duplicate enrollment prevention
- stronger validation for business rules

---

# Why This Project Is Strong for QA Portfolio

This project demonstrates:

- real CRUD implementation
- SQL database validation
- API testing understanding
- business logic verification
- backend consistency checks
- enterprise SaaS style testing approach

This is much stronger than simple demo CRUD projects and much closer to real QA work in production systems.