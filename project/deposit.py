#!/usr/bin/python3
"""
Defines the Deposit Process
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Deposits, Accounts

# contains string for the database
str1 = 'mysql://root:""@localhost:3306/WEKEZA'
# creates a connection to our database
engine = create_engine(str1)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def deposit(user_details):
    """
    Asks user for amount to deposit then checks
    if it is less than 500 if so requests user to deposit
    again or exit deposit function else deposits 
    amount user enters
    """
    # stores the user details for recalling deposit
    amn_to_dep = int(input("Enter Amount To Deposit: "))
    if amn_to_dep <= 500:
        print("You can only deposit > 500\=")
        deposit(user_details)
    else:
        results = session.query(Accounts).filter(Accounts.user_id
                  == user_details.user_id).first()
        dep_1 = Deposits()
        dep_1.user_id = user_details.user_id
        dep_1.amt_deposited = amn_to_dep
        balance = results.acc_balance + amn_to_dep
        results.acc_balance = balance
        dep_1.acc_balance = balance
        session.add(dep_1)
        session.commit()
        print("Successful")

