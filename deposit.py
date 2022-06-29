#!/usr/bin/python3
"""
Defines the Deposit Process
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import User

# contains string for the database
str1 = 'mysql://root:""@localhost:3306/WEKEZA'
# creates a connection to our database
engine = create_engine(str1)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def deposit():
    """
    Asks user for amount to deposit then checks
    if it is less than 500 if so requests user to deposit
    again or exit deposit function else deposits 
    amount user enters
    """
    amn_to_depo = int(input("Enter Amount To Deposit: "))
    if amn_to_depo <= 500:
        print("You can only deposit > 500\=")
        deposit()
    else:

