from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Вказуємо, що наша база буде зберігатися у файлі blog.db
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

# Створюємо "двигун", який буде підключатися до бази
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Створюємо сесію (канал зв'язку з базою)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовий клас для створення наших таблиць
Base = declarative_base()