## Enrollments CRUD + Business Logic

### What was implemented

Created a new business entity: `enrollments`

This table connects:
- users
- courses

and represents course progress tracking inside LMS.

This is much stronger than simple CRUD because it includes real business logic.

---

## Enrollment Model

File:
app/models/enrollment.py

Fields:

- id
- user_id (FK → users.id)
- course_id (FK → courses.id)
- progress
- status
- certificate_issued
- enrolled_at
- completed_at

Business meaning:

- progress → course completion percentage
- status → in_progress / completed
- certificate_issued → whether certificate was granted
- completed_at → completion datetime

---

## Enrollment Schemas

File:
app/schemas/enrollment.py

Created:

### EnrollmentCreate

Used for POST request

Required:

- user_id
- course_id

Default values:

- progress = 0
- status = "in_progress"
- certificate_issued = False

---

### EnrollmentResponse

Used for API response

Includes:

- id
- user_id
- course_id
- progress
- status
- certificate_issued
- enrolled_at
- completed_at

---

### EnrollmentUpdate

Used for PATCH request

Optional fields:

- progress
- status
- certificate_issued

This allows partial update.

Example:

{
  "progress": 100
}

---

## CRUD Endpoints

File:
app/routes/enrollment.py

Implemented:

### POST /enrollments/

Create enrollment

Business logic:

If:

progress == 100

Then automatically:

- status = "completed"
- certificate_issued = True
- completed_at = current datetime

Else:

- status = "in_progress"
- certificate_issued = False
- completed_at = NULL

This prevents invalid manual input.

---

### GET /enrollments/

Get all enrollments

Used for checking all user-course relations.

---

### GET /enrollments/{id}

Get enrollment by ID

If enrollment does not exist:

404 → Enrollment not found

---

### PATCH /enrollments/{id}

Partial update

Main QA case:

Example:

{
  "progress": 100
}

System automatically updates:

- status
- certificate
- completed_at

Also handles reverse logic:

If progress becomes < 100:

- status = "in_progress"
- certificate_issued = False
- completed_at = NULL

This is real business validation.

---

### DELETE /enrollments/{id}

Delete enrollment

Validation:

If enrollment not found:

404 → Enrollment not found

Success response:

{
  "message": "Enrollment deleted successfully"
}

---

## Important QA Learning

This entity is not simple CRUD.

It demonstrates:

- business rules validation
- state transitions
- system-generated values
- negative scenarios
- backend consistency checks

Very strong interview example for:

- API testing
- business logic testing
- Postman
- SQL validation
- edge cases testing

This is much closer to real production QA work.