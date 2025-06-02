from fastapi import FastAPI
from server.api import users
from server.db.session import engine, Base

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management API", version="1.0.0")

# 라우터 등록
app.include_router(users.router, prefix="/api/v1", tags=["users"])
