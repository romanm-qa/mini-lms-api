## CRUD for Courses (Fake in-memory database)

### What we implemented

Instead of a real database, we temporarily use:

courses = []

This is a fake in-memory storage:
- data exists only while server is running
- after restart everything is deleted
- useful for learning API logic before connecting real DB

---

## Endpoints

### POST /courses

Create new course.

Logic:
- receive request body: title, description, is_active
- convert Pydantic object to dictionary using: course.model_dump()
- generate fake ID: new_course["id"] = len(courses) + 1
- save into fake database: courses.append(new_course)
- return created object

---

### GET /courses

Get all courses.

Logic:
- return full list of courses: return courses

---

### GET /courses/{course_id}

Get course by ID.

Logic:
- receive course_id from URL path
- loop through all courses
- compare course["id"] == course_id
- if found, return course
- if not found, return 404:

raise HTTPException(status_code=404, detail="Course not found")

---

### PUT /courses/{course_id}

Update existing course by ID.

Logic:
- receive course_id from URL path
- receive updated body: title, description, is_active
- find course by ID
- update fields: title, description, is_active
- return updated course
- if not found, return 404

---

### DELETE /courses/{course_id}

Delete course by ID.

Logic:
- receive course_id from URL path
- find course by ID
- remove from list: courses.remove(course)
- return success message: {"message": "Course deleted successfully"}
- if not found, return 404

---

## Result

Full CRUD completed:
- Create: POST /courses
- Read all: GET /courses
- Read one: GET /courses/{course_id}
- Update: PUT /courses/{course_id}
- Delete: DELETE /courses/{course_id}

Swagger successfully tested for all endpoints.