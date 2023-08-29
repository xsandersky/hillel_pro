import uuid
from typing import List, Optional
from sqlalchemy import ForeignKey, String, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://vitalii:1325@localhost:5432/books",
    isolation_level="SERIALIZABLE", echo=True)




