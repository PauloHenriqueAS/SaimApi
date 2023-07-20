"""
main.py

COnfigurations of FastAPI
"""

from fastapi import FastAPI
from app import (
    user_router,
    health_router,
    person_router,
    image_router,
    process_router,
    dashboard_router
)

app = FastAPI(
    title="SaimAPI",
    description="SaimAPI - Processamento de Imagens de Madeira",
    version="1.0.0",
    )

app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(health_router, tags=["HealthCheck"])
app.include_router(person_router, prefix="/person", tags=["Person"])
app.include_router(image_router, prefix="/image", tags=["Image"])
app.include_router(process_router, prefix="/process", tags=["Image Process"])
app.include_router(dashboard_router, prefix="/dashboard", tags=["Dashboard"])
