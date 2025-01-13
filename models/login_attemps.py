from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from models.base import Base
from datetime import datetime
from uuid import uuid4
from sqlalchemy.types import LargeBinary 

class Login_attemps(Base):
    __tablename__ = "login_attemps"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    timestamp = Column(DateTime(), default=datetime.now())