from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import Boolean
from sqlalchemy import BigInteger
from sqlalchemy import DateTime
import datetime
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    username = Column(String)
    age = Column(Integer)
    city = Column(String)
    field = Column(String)
    about = Column(String)
    active = Column(Boolean, default=True)
