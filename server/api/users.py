from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from server.db.session import get_db
from server.schemas.user import UserCreate, UserResponse
from server.crud.user import get_user_by_email, get_user_by_nickname, validate_password, create_user, activate_user_by_token
from server.core.token import generate_email_token
from server.services.email import send_verification_email

router = APIRouter(prefix="/auth")

@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="이미 존재하는 이메일입니다.")
    
    if get_user_by_nickname(db, user.nick_name):
        raise HTTPException(status_code=400, detail="이미 존재하는 닉네임입니다.")
    
    validate_password(user.password)

    token = generate_email_token()
    db_user = create_user(db, user, token)
    background_tasks.add_task(send_verification_email, db_user.email, token)
    return db_user

@router.get("/verify-email")
def verify_email(token: str, db: Session = Depends(get_db)):
    user = activate_user_by_token(db, token)
    if not user:
        raise HTTPException(status_code=400, detail="유효하지 않은 토큰입니다.")
    return {"message": "이메일 인증이 완료되었습니다."}

