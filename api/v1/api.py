from fastapi import APIRouter
from .endpoints import (user,calc)

api_router = APIRouter()

api_router.include_router(
        user.router,
        prefix="/user",
        tags=["User"]
    )
api_router.include_router(
        calc.router,
        prefix="/calc",
        tags=["Calc"]
    )


