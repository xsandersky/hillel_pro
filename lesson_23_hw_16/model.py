import uuid
from typing import List, Optional
from sqlalchemy import  String, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = 'books'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4())
    name: Mapped[List[str]] = mapped_column((String(50)))
    author: Mapped[str] = mapped_column((String(30)))
    date_of_release: Mapped[Date] = mapped_column(Date)
    description: Mapped[Optional[str]] = mapped_column(String(500))
    genre: Mapped[str] = mapped_column(String(30))
