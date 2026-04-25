from pydantic import BaseModel, EmailStr
from typing import List, Optional

# Схема для Постів (що ми бачимо в пості)
class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

# Схема для Користувачів
class UserBase(BaseModel):
    email: EmailStr
    username: str

# Це те, що ми просимо при реєстрації (тут є пароль)
class UserCreate(UserBase):
    password: str

# Це те, що ми повертаємо (тут ПАРОЛЯ НЕМАЄ - це безпека!)
class User(UserBase):
    id: int
    posts: List[Post] = []

    class Config:
        from_attributes = True