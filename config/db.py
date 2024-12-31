from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

# Crear una clase de sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
