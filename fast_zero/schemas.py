from pydantic import BaseModel, EmailStr, ConfigDict

class UserSchema(BaseModel):
    username: str
    password: str
    email: EmailStr

class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    user_id: int
    access_token: str
    token_type: str