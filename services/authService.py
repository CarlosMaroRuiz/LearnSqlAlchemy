from sqlalchemy.orm import Session
from schemas.userSchema import UserCreate
from bd.models.user import User
from fastapi import HTTPException, status
from utils.security import verify_password
from auth.generateToken import generateToken
def loguearse(user: UserCreate, db: Session):
    db_user = db.query(User).filter(User.correo == user.correo).first()
    
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El correo no está registrado"
        )
    
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Contraseña incorrecta"
        )
    
    return generateToken(data={"correo":user.correo})
