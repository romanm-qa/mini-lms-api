from pydantic import BaseModel
from datetime import datetime


class EnrollmentCreate(BaseModel):
    user_id: int
    course_id: int
    progress: int = 0
    status: str = "in_progress"
    certificate_issued: bool = False


class EnrollmentResponse(BaseModel):
    id: int
    user_id: int
    course_id: int
    progress: int
    status: str
    certificate_issued: bool
    enrolled_at: datetime
    completed_at: datetime | None = None


class EnrollmentUpdate(BaseModel):
    progress: int | None = None
    status: str | None = None
    certificate_issued: bool | None = None