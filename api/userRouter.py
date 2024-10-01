from fastapi import APIRouter,Depends,HTTPException
from schemas.userSchema import UserResponse,UserCreate,User
from sqlalchemy.orm import Session
from bd.session import get_db
from services.userService import createUser,getUsers
""" 
Depends() es utilizada para inyección de dependencias.
Es una poderosa característica que te permite declarar dependencias de manera 
explícita en tus rutas, manejadores y funciones. Las dependencias pueden ser
cualquier cosa que necesites en la ejecución de una ruta, 
como sesiones de base de datos, autenticación,
validación o cualquier otra lógica.
"""



router = APIRouter()
""" 
response_model=UserResponse 
para asegurarse de que la respuesta 
que se devuelve al cliente sigue el esquema 
definido en UserResponse
"""

@router.get("/",response_model=list[User])
def get_user(db: Session = Depends(get_db)):
    users = getUsers(db)
    return users
    
@router.post("/create/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = createUser(user=user, db=db) 
        return UserResponse(correo=db_user.correo,msg="usuario creado correctamente")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear el usuario")



    