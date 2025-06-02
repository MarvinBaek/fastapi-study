from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    nick_name: str | None = None
    phone_number: str | None = None

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    nick_name: str | None = None
    is_active: bool
    is_admin: bool

    class Config:
        from_attributes = True
