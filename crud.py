from sqlalchemy.orm import Session
import models, schemas

# --- РОБОТА З КОРИСТУВАЧАМИ ---

# Знайти користувача за поштою
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Створити нового користувача
def create_user(db: Session, user: schemas.UserCreate):
    # У реальному житті тут ми б ще хешували пароль, але для 1-ї лабораторної
    # зробимо просто, щоб не ускладнювати вам запуск
    fake_hashed_password = user.password + "notreallyhashed"
    
    db_user = models.User(
        email=user.email, 
        username=user.username, 
        hashed_password=fake_hashed_password
    )
    db.add(db_user)
    db.commit()      # Зберігаємо в базу
    db.refresh(db_user) # Оновлюємо дані
    return db_user

# --- РОБОТА З ПОСТАМИ ---

# Створити пост для конкретного користувача
def create_user_post(db: Session, post: schemas.PostCreate, user_id: int):
    db_post = models.Post(**post.dict(), owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# Отримати список усіх постів
def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()