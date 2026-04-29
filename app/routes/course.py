from fastapi import APIRouter
from app.schemas.course import CourseCreate

router = APIRouter()


@router.post("/courses")
def create_course(course: CourseCreate):
    return {
        "message": "Course created successfully",
        "data": course
    }