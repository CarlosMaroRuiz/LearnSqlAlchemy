from sqlalchemy.orm import Session
from schemas.userSchema import UserCreate
from bd.models.user import User
from utils.security import hash_password
from fastapi import HTTPException

def createUser(db: Session, user: UserCreate):
    try:
        # Hashear la contraseña antes de guardarla
        hashed_password = hash_password(user.password)
        
        # Crear el objeto de usuario con la contraseña hasheada
        db_user = User(correo=user.correo, hashed_password=hashed_password)
        db.add(db_user)
        
        
        db.commit()
        db.refresh(db_user) 
        
        return db_user
    except Exception as e:
        
        db.rollback()

        raise HTTPException(status_code=400, detail=f"Error al crear el usuario: {str(e)}")


def getUsers(db:Session):
    datos =   db.query(User).all()
    return datos
    
