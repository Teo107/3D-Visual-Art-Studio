from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    canvases = relationship("Canvas", back_populates="owner")

class Canvas(Base):
    __tablename__ = "canvases"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    data = Column(JSON)  # Stores the complex JSON arrays of 3D coordinates (x, y, z)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="canvases")
