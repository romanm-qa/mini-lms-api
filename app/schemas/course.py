from datetime import datetime
from pydantic import BaseModel


class CourseCreate(BaseModel):
    title: str
    description: str
    category: str
    level: str
    duration_minutes: int
    price: int
    is_active: bool = True


class CourseUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    category: str | None = None
    level: str | None = None
    duration_minutes: int | None = None
    price: int | None = None
    is_active: bool | None = None


class CourseResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    level: str
    duration_minutes: int
    price: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }