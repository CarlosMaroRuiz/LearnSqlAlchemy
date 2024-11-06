from fastapi import FastAPI
from api import userRouter,fileRouter

app = FastAPI()

#añadimos todas nuestras rutas de api
app.include_router(userRouter.router, prefix="/users", tags=["users"])
app.include_router(fileRouter.router, prefix="/upload", tags=["upload"])
#para ejecutar la app para 3 workers
#uvicorn main:app --host 0.0.0.0 --port 5000 --workers 3