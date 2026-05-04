from pydantic import BaseModel


class CourseCreate(BaseModel):
    title: str
    description: str | None = None
    is_active: bool = True


class CourseUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    is_active: bool | None = None


class CourseResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    is_active: bool

    model_config = {
        "from_attributes": True
    }