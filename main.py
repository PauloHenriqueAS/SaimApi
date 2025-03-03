"""
main.py

COnfigurations of FastAPI
"""


from fastapi import FastAPI
#from .jwt import TokenRequest, Token
from fastapi.middleware.cors import CORSMiddleware

from app import (
    user_router,
    health_router,
    person_router,
    image_router,
    process_router,
    dashboard_router,
    #authentication_router
)

app = FastAPI(
    title="SaimAPI",
    description="SaimAPI - Processamento de Imagens de Madeira",
    version="1.0.0",
    swagger_favicon_url="../favicon.png",
    )

# Configurar CORS (para permitir solicitações de diferentes origens)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Atualize isso para limitar as origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Importar e usar as rotas de autenticação
#from .jwt import login_for_access_token, protected_route

#app.include_router(authentication_router, prefix="/authentication", tags=["Authentication"])
app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(health_router, tags=["HealthCheck"])
app.include_router(person_router, prefix="/person", tags=["Person"])
app.include_router(image_router, prefix="/image", tags=["Image"])
app.include_router(process_router, prefix="/process", tags=["Image Process"])
app.include_router(dashboard_router, prefix="/dashboard", tags=["Dashboard"])

# @app.on_event("startup")
# async def startup():
#     await database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()
    