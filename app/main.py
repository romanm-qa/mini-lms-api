from fastapi import FastAPI

from app.routes.course import router as course_router
from app.routes.users import router as users_router
from app.database import engine, Base
from app.models.course import Course
from app.models.user import User
from app.models.enrollment import Enrollment
from app.routes.enrollment import router as enrollment_router


app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(course_router)
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(
    enrollment_router,
    prefix="/enrollments",
    tags=["Enrollments"]
)


@app.get("/health")
def health_check():
    return {"status": "ok"}