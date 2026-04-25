from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# --- ТАБЛИЦЯ КОРИСТУВАЧІВ ---
class User(Base):
    __tablename__ = "users"

    # Колонки нашої таблиці
    id = Column(Integer, primary_key=True, index=True)      # Унікальний номер
    email = Column(String, unique=True, index=True)         # Пошта (має бути унікальною)
    username = Column(String, unique=True, index=True)      # Логін
    hashed_password = Column(String)                        # Зашифрований пароль

    # Зв'язок: один користувач може мати багато написаних постів
    posts = relationship("Post", back_populates="owner")


# --- ТАБЛИЦЯ ПОСТІВ (ЗАПИСІВ БЛОГУ) ---
class SurveyResponsest(Base):
    __tablename__ = "posts"

    # Колонки таблиці
    id = Column(Integer, primary_key=True, index=True)      # Номер поста
    title = Column(String, index=True)                      # Заголовок
    content = Column(String)                                # Текст поста
    owner_id = Column(Integer, ForeignKey("users.id"))      # Посилання на автора (його id)

    # Зв'язок: цей пост належить конкретному користувачу
    owner = relationship("User", back_populates="posts")