from sqlalchemy.orm import Session
from passlib.context import CryptContext
from server.models.user import User
from server.schemas.user import UserCreate
import re
from fastapi import HTTPException, status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_nickname(db: Session, nickname: str):
    return db.query(User).filter(User.nick_name == nickname).first()


def validate_password(password: str):
    #최소 8자 이상, 대문자, 소문자, 숫자, 특수문자 포함
    if len(password) < 8:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="비밀번호는 최소 8자 이상이어야 합니다.")
    
    if not re.search(r"[A-Z]", password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="비밀번호에 최소 한 개의 대문자가 포함되어야 합니다.")
    
    if not re.search(r"[a-z]", password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="비밀번호에 최소 한 개의 소문자가 포함되어야 합니다.")
    
    if not re.search(r"[0-9]", password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="비밀번호에 최소 한 개의 숫자가 포함되어야 합니다.")
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="비밀번호에 최소 한 개의 특수문자가 포함되어야 합니다.")

def create_user(db: Session, user: UserCreate, email_token: str):
    hashed_pw = pwd_context.hash(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_pw,
        nick_name=user.nick_name,
        phone_number=user.phone_number,
        email_verify_token=email_token,
        is_active=False,
        is_admin=False
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def activate_user_by_token(db: Session, token: str):
    user = db.query(User).filter(User.email_verify_token == token).first()
    if user:
        user.is_active = True
        user.email_verify_token = None
        db.commit()
    return user
