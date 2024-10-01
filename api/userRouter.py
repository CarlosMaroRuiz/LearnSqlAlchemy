from fastapi import APIRouter,Depends,HTTPException,Request
from schemas.userSchema import UserResponse,UserCreate,User
from sqlalchemy.orm import Session
from bd.session import get_db
from services.userService import createUser,getUsers
from schemas.tokenSchema import Token
from services.authService import loguearse
from auth.decoderToken import get_current_user

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

@router.get("/", response_model=list[User])
async def get_user(request: Request, db: Session = Depends(get_db),token: str = Depends(get_current_user)):
    try:
        users = getUsers(db)  # Obtenemos los usuarios desde el servicio
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener usuarios: {str(e)}")
    
@router.post("/create/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = createUser(user=user, db=db) 
        return UserResponse(correo=db_user.correo,msg="usuario creado correctamente")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear el usuario")
    
@router.post("/login/",response_model =Token)
def login(user:UserCreate,db:Session = Depends(get_db)):
    try:
        userFind = loguearse(user,db)
        return Token(access_token=userFind)
    
    except Exception as e:
        raise e
    



    