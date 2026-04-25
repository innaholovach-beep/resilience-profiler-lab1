from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

# Створюємо базу даних
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Блог: Лабораторна №1")

# Підключення до БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Вітаю! Це ваш блог. Лабораторна №1 виконана."}

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/users/{user_id}/posts/", response_model=schemas.Post)
def create_post_for_user(user_id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_user_post(db=db, post=post, user_id=user_id)

@app.get("/posts/", response_model=list[schemas.Post])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_posts(db, skip=skip, limit=limit)