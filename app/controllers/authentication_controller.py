from datetime import timedelta, datetime
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from jose import JWTError, jwt
from passlib.context import CryptContext

from SaimApi.app.services import user_service

# to get a string like this run:
# openssl rand -hex 32
#Adicionar essas informações no json de configuração
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()
# jwt.py

from fastapi import HTTPException, Depends
from jose import JWTError, jwt
from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str

class UserInDB(User):
    hashed_password: str

class UserCreate(User):
    password: str

class UserOut(User):
    id: int
    username: str

# Função para criar token JWT
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Função para verificar token JWT
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    return token_data

# Senha de exemplo (NÃO use isso em produção, use um mecanismo de armazenamento seguro de senhas)
fake_users_db = {}

# Configurar função de verificação de senha
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Configurar função para obter usuário pelo nome de usuário
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserOut(**user_dict)

# Configurar função para autenticar usuário
def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return None
    if not user_service.autenticate_user(password, user.hashed_password):
        return None
    return user

# Configurar classe de solicitação de token
class TokenRequest(BaseModel):
    username: str
    password: str

# Configurar função para criar token
@app.post("/token", response_model=Token)
async def login_for_access_token(token_request: TokenRequest):
    user = authenticate_user(fake_users_db, token_request.username, token_request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Configurar rota protegida que requer autenticação
@app.get("/protected-route")
async def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": "This is a protected route", "current_user": current_user}
