#!/usr/bin/python3
"""
defines a class User
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()
# contains string for the database
str1 = 'mysql://root:""@localhost:3306/WEKEZA'
# creates a connection to our database
engine = create_engine(str1)


class User(Base):
    """
    Table for Users
    """
    __tablename__ = "Users"
    user_id = Column(Integer, primary_key=True)
    username = Column(String(50))
    firstname = Column(String(50))
    lastname = Column(String(50))
    id_no = Column(Integer, nullable=False)
    PhoneNumber = Column(Integer)
    Password = Column(String(50))

Base.metadata.create_all(engine)
