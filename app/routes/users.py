from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.user import User as UserSchema, UserUpdate
from app.models.user import User as UserModel


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    new_user = UserModel(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        role=user.role,
        progress=user.progress,
        certificate=user.certificate,
        is_active=user.is_active,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully", "user": new_user}

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(UserModel).all()


@router.get("/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()

    if user is None:
        return {"message": "User not found"}

    return user

@router.put("/{user_id}")
def update_user_progress(
    user_id: int,
    progress: int,
    db: Session = Depends(get_db)
):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()

    if user is None:
        return {"message": "User not found"}

    user.progress = progress

    if progress == 100:
        user.certificate = True

    db.commit()
    db.refresh(user)

    return {
        "message": "User updated successfully",
        "user": user
    }

@router.patch("/{user_id}")
def patch_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()

    if user is None:
        return {"message": "User not found"}

    update_data = user_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(user, key, value)

    if "progress" in update_data and user.progress == 100:
        user.certificate = True

    db.commit()
    db.refresh(user)

    return {
        "message": "User updated successfully",
        "user": user
    }

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()

    if user is None:
        return {"message": "User not found"}

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}