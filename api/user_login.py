from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from model.user_login import User
from Schema.user_login import UserLogin,UserRegister,UserResponse

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=201)
async def register_user(user: UserRegister, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create new user
    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password,  # You should hash this in production
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login", status_code=200)
async def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    if db_user.is_deleted:
        raise HTTPException(status_code=404, detail="User is deleted")
    if user.password != db_user.password:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    return {
        "status": "success",
        "id": db_user.id,
        "username": db_user.name,
        "email": db_user.email,
        "role": db_user.role
    }


