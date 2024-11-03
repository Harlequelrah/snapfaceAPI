from sqlalchemy import (
    Boolean,
    Column,
    DECIMAL,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Table,
)
from settings.database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class SnapFace(Base):
    __tablename__="snapfaces"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(100),nullable=False)
    description = Column(String(200), nullable=False)
    snaps=Column(Integer,default=0)
    imageUrl=Column(String(256))
    location=Column(String(256),nullable=True)
    createdAt=Column(DateTime,nullable=False,default=func.now())
