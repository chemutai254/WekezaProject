#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Accounts

# contains string for the database
str1 = 'mysql://root:""@localhost:3306/WEKEZA'
# creates a connection to our database
engine = create_engine(str1)
DBSession = sessionmaker(bind=engine)
session = DBSession()

results = session.query(Accounts).filter(Accounts.acc_id == 1).first()
print(type(results.acc_balance))

