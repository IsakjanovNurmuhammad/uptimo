from pydantic import BaseModel, Field, EmailStr


class CreateUser(BaseModel):
    username: str
    email: EmailStr = Field(..., nullable=True, index=True, unique=True)
    password: str


class InfoOut(BaseModel):
    name: str
    course: str
    phone_number: str

