# Mini LMS API

Mini LMS API is a practice project built for improving QA skills in:

* API testing
* Postman practice
* SQL validation
* backend architecture understanding
* QA automation preparation

The goal of this project is not only to write API endpoints, but to deeply understand how backend systems work and how QA engineers test them in real projects.

---

# Project Goals

This project helps practice:

* FastAPI fundamentals
* request / response validation
* routes and routers
* Swagger / OpenAPI documentation
* Postman API testing
* SQLAlchemy and database logic
* CRUD operations
* API automation with pytest + requests
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
* POST `/courses` endpoint
* request body validation using Pydantic schemas
* automatic Swagger documentation
* architecture notes for interview preparation

---

# Project Structure

```text
mini-lms-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   │
│   ├── routes/
│   │   └── course.py
│   │
│   ├── schemas/
│   │   └── course.py
│   │
│   └── models/
│
├── tests/
│   └── api/
│
├── notes/
│   ├── schemas_and_validation.md
│   ├── routes_and_routers.md
│   └── swagger_and_postman.md
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Why This Project Matters for QA

This is not just a coding exercise.

It is a QA-focused backend project created to:

* understand how APIs are built
* improve API testing confidence
* prepare stronger interview answers
* practice real-world backend validation
* build a strong GitHub portfolio project

This helps bridge the gap between manual QA and automation QA.

---

# Next Steps

Planned implementation:

* GET all courses
* GET course by ID
* UPDATE course
* DELETE course
* database integration
* SQLAlchemy models
* automated API tests
* negative and validation scenarios
* authentication testing

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
