from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from datetime import datetime

from app.database import Base


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)

    progress = Column(Integer, default=0)
    status = Column(String, default="in_progress")
    certificate_issued = Column(Boolean, default=False)

    enrolled_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)