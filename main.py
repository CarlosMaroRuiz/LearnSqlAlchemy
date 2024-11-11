from fastapi import FastAPI
from api import userRouter,fileRouter
from middleware.cors_middleware import CustomCORSMiddleware
from middleware.rate_limiter_middleware import RateLimitMiddleware
app = FastAPI()

#middlewares
app.add_middleware(CustomCORSMiddleware)
app.add_middleware(RateLimitMiddleware,max_requests=5, period=60)

#añadimos todas nuestras rutas de api
app.include_router(userRouter.router, prefix="/users", tags=["users"])
app.include_router(fileRouter.router, prefix="/upload", tags=["upload"])
#para ejecutar la app para 3 workers
#uvicorn main:app --host 0.0.0.0 --port 5000 --workers 3
