from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


DATABASE_URL = "sqlite:///./tareas.db"

engine = create_engine(  
DATABASE_URL,
connect_args={"check_same_thread": False} 
) # Solo para SQLite

SesionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine)


Base = declarative_base()

def get_db():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()