from fastapi import APIRouter, HTTPException
from app.schemas.course import CourseCreate, CourseResponse

router = APIRouter()

courses = []

# GET all courses
@router.get("/courses", response_model=list[CourseResponse])
def get_courses():
    return courses

# GET course by ID
@router.get("/courses/{course_id}", response_model=CourseResponse)
def get_course(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return course

    raise HTTPException(status_code=404, detail="Course not found")

# PUT update course by ID
@router.put("/courses/{course_id}", response_model=CourseResponse)
def update_course(course_id: int, updated_course: CourseCreate):
    for course in courses:
        if course["id"] == course_id:
            course["title"] = updated_course.title
            course["description"] = updated_course.description
            course["is_active"] = updated_course.is_active
            return course

    raise HTTPException(status_code=404, detail="Course not found")

# DELETE course by ID
@router.delete("/courses/{course_id}")
def delete_course(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            courses.remove(course)
            return {"message": "Course deleted successfully"}

    raise HTTPException(status_code=404, detail="Course not found")

# POST create new course
@router.post("/courses", response_model=CourseResponse)
def create_course(course: CourseCreate):
    new_course = course.model_dump()

# generate fake ID    
    new_course["id"] = len(courses) + 1

# save course to fake database (temporary in-memory storage)
    courses.append(new_course)

    return new_course