#!/usr/bin/python3
"""
Defines the Withdrawal Process
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Withdrawals, Accounts

# contains string for the database
str1 = 'mysql://root:""@localhost:3306/WEKEZA'
# creates a connection to our database
engine = create_engine(str1)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def withdraw(user_details):
    """
    Asks user for amount to withdraw then checks
    if it is less than account balance. If it is less
    it displays account balance plus a message

    args:
        user_details:contains details about the logged
        in user
    """
    # stores users details for recalling withdraw
    copy = user_details

    amn_to_withdr = int(input("Enter Amount To Withdraw: "))
    results = session.query(Accounts).filter(Accounts.user_id
        == user_details.user_id).first()

    if amn_to_withdr > results.acc_balance:
        print("Insufficient Funds")
        print("Your Account Balance is ", end='')
        print(results.acc_balance)
    else:
        withdraw_1 = Withdrawals()
        withdraw_1.user_id = user_details.user_id
        withdraw_1.amt_withdrawn = amn_to_withdr
        balance = results.acc_balance - amn_to_withdr
        results.acc_balance = balance
        withdraw_1.acc_balance = balance
        session.add(withdraw_1)
        session.commit()
        print("Successfully Withdrawn: ",end='')
        print(withdraw_1.amt_withdrawn)
