from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.enrollment import Enrollment as EnrollmentModel
from app.schemas.enrollment import EnrollmentCreate, EnrollmentResponse, EnrollmentUpdate
from datetime import datetime

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=EnrollmentResponse)
def create_enrollment(
    enrollment: EnrollmentCreate,
    db: Session = Depends(get_db)
):

    status = enrollment.status
    certificate_issued = enrollment.certificate_issued
    completed_at = None

    if enrollment.progress == 100:
        status = "completed"
        certificate_issued = True
        completed_at = datetime.utcnow()

    new_enrollment = EnrollmentModel(
        user_id=enrollment.user_id,
        course_id=enrollment.course_id,
        progress=enrollment.progress,
        status=status,
        certificate_issued=certificate_issued,
        completed_at=completed_at
    )

    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)

    return new_enrollment


@router.get("/", response_model=list[EnrollmentResponse])
def get_enrollments(db: Session = Depends(get_db)):
    return db.query(EnrollmentModel).all()


@router.get("/{enrollment_id}", response_model=EnrollmentResponse)
def get_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    enrollment = db.query(EnrollmentModel).filter(
        EnrollmentModel.id == enrollment_id
    ).first()

    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")

    return enrollment


@router.patch("/{enrollment_id}", response_model=EnrollmentResponse)
def patch_enrollment(
    enrollment_id: int,
    enrollment_data: EnrollmentUpdate,
    db: Session = Depends(get_db)
):
    enrollment = db.query(EnrollmentModel).filter(
        EnrollmentModel.id == enrollment_id
    ).first()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    update_data = enrollment_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(enrollment, key, value)

    if enrollment.progress == 100:
        enrollment.status = "completed"
        enrollment.certificate_issued = True
        enrollment.completed_at = datetime.utcnow()
    else:
        enrollment.status = "in_progress"
        enrollment.certificate_issued = False
        enrollment.completed_at = None

    db.commit()
    db.refresh(enrollment)

    return enrollment


@router.delete("/{enrollment_id}")
def delete_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    enrollment = db.query(EnrollmentModel).filter(
        EnrollmentModel.id == enrollment_id
    ).first()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    db.delete(enrollment)
    db.commit()

    return {"message": "Enrollment deleted successfully"}