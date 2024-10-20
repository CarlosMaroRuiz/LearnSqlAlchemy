from pydantic import BaseModel,EmailStr


class UserCreate(BaseModel):
    correo: EmailStr
    password: str

class UserResponse(BaseModel):
    correo: str
    msg: str
    
class User(BaseModel):
    correo:str

    class Config:
        from_attributes = True
