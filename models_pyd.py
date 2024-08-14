from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    description: str = ''

class PostUpdate(BaseModel):
    title: str
    description: str = ''



class UserCreate(BaseModel):
    name: str
    surname: str

class UserUpdate(BaseModel):
    name: str
    surname: str