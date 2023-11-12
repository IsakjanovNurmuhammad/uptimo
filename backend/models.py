from Database import Base
from sqlalchemy import Integer, String, Column


class UserInfo(Base):
    __tablename__ = "infos"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    course = Column(String)
    phone_number = Column(String)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=False)
    password = Column(String)


