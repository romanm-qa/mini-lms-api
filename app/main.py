from fastapi import FastAPI
from app.routes.course import router as course_router

app = FastAPI()

app.include_router(course_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}