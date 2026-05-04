from fastapi import FastAPI

from app.routes.course import router as course_router
from app.database import engine, Base
from app.models.course import Course


app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(course_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}