# from fastapi import APIRouter, Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from typing import Annotated
# from jose import JWTError, jwt
# from passlib.context import CryptContext

# # to get a string like this run:
# # openssl rand -hex 32
# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# router = APIRouter()

# # Simulação de usuários registrados (apenas para fins de exemplo)
# fake_users = {
#     "johndoe": {
#         "username": "johndoe",
#         "password": "password123"
#     }
# }

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# @router.post("/token", response_model=Token)
# async def login_for_access_token(
#     form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
# ):
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}


# @router.post("/AutenticateUser")
# def autenticate_user(token: Annotated[str, Depends(oauth2_scheme)]):
#     """
#     Return confirmation if user is authenticated
#     """
#     user = fake_decode_token(token)
#     return f"teste: {user}"

# def fake_decode_token(token):
#     return {"username": token + "fakedecoded", "email": "john@example.com", "full_name": "John Doe"}

# def authenticate_user(username: str, password: str):
#     if username in fake_users and fake_users[username]["password"] == password:
#         return True
#     return False

# @router.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     username = form_data.username
#     password = form_data.password

#     if not authenticate_user(username, password):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")

#     return {"access_token": username, "token_type": "bearer"}
