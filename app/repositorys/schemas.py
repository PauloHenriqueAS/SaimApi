# from typing import List, Optional, Generic, TypeVar
# from pydantic import BaseModel, Field

# T = TypeVar('T')

# class UserSchema(BaseModel):
#     id_user = int 
#     email_user = str
#     password_user = str

#     class Config:
#         orm_mode = True

# class RequestUser(BaseModel):
#     parameter: UserSchema = Field(...)
