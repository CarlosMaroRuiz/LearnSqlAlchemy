from fastapi import FastAPI
from api import userRouter

app = FastAPI()

#añadimos todas nuestras rutas de api
app.include_router(userRouter.router, prefix="/users", tags=["users"])
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)