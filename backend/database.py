import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Use environment variable for database URL, with a fallback for local development
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://art_user:Art_studio_pass@localhost:5433/art_studio_db")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
