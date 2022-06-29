#!/usr/bin/python3
"""
defines a class User
"""

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, LargeBinary, ForeignKey
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import relationship


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
    Password = Column(String(100))


class Accounts(Base):
    """
    Table for Accounts
    """
    __tablename__ = "Accounts"
    acc_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'))
    acc_balance = Column(Integer, default=0)
    user = relationship("User", back_populates="account")


User.account = relationship("Accounts", back_populates="user")

class Registration(Base):
    """
    Table for Registration Details
    """
    __tablename__ = "Registration"
    reg_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'))
    registrationfee = Column(Integer, default=1000)
    user = relationship("User", back_populates="registration")


User.registration = relationship("Registration", back_populates="user")


class Deposits(Base):
    """
    Table for Deposits Details
    """
    __tablename__ = "Deposits"
    dep_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'))
    dep_date = Column(DateTime, default=datetime.now())
    amt_deposited = Column(Integer)
    acc_balance = Column(Integer)
    user = relationship("User", back_populates="deposit")


User.deposit = relationship("Deposits", back_populates="user")


class Withdrawals(Base):
    """
    Table for Withdrawal details
    """
    __tablename__ = "Withdrawals"
    withd_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'))
    withd_date = Column(DateTime, default=datetime.now())
    amt_withdrawn = Column(Integer)
    acc_balance = Column(Integer)
    user = relationship("User", back_populates="withdraw")


User.withdraw = relationship("Withdrawals", back_populates="user")


Base.metadata.create_all(engine)
