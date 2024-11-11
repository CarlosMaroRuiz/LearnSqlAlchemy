from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from time import time
from collections import defaultdict


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int = 5, period: int = 60):
        super().__init__(app)
        self.max_requests = max_requests
        self.period = period
        self.requests = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host  # Obtener la IP del cliente
        current_time = time()

        self.requests[client_ip] = [
            timestamp for timestamp in self.requests[client_ip]
            if timestamp > current_time - self.period
        ]

        if len(self.requests[client_ip]) >= self.max_requests:
            return JSONResponse(status_code=429, content={"detail": "Too Many Requests"})

        self.requests[client_ip].append(current_time)
        response = await call_next(request)
        return response
