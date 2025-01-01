from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from models.base import Base
from datetime import datetime
from uuid import uuid4
from sqlalchemy.types import LargeBinary  

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    first_names = Column(String(50))
    last_names = Column(String(50))
    username = Column(String(15), nullable=False)
    email = Column(String, unique=True)
    password = Column(LargeBinary, nullable=False)
    created_at = Column(DateTime(), default=datetime.now())
