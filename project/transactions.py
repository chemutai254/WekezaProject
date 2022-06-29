#!/usr/bin/python3
"""
Defines Function Transaction
"""
#!/usr/bin/python3
"""
Defines the Deposit Process
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Deposits, Accounts, Withdrawals

# contains string for the database
str1 = 'mysql://root:""@localhost:3306/WEKEZA'
# creates a connection to our database
engine = create_engine(str1)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def transactions(arg, user_details):
    """
    Used to query the database to print User details
    such withdrawals made, deposits made, account balance

    args:
        arg(int):determine which transactions  to do
                case 3 Checks Balance case
                case 4 Checks Withdrawals History
                case 5 Checks Deposit History
        user_details: holds details for logged in user
    """
    if arg == 3:
        results = session.query(Accounts).filter(Accounts.user_id
           == user_details.user_id).first()
        print("Your Account Balance is: ", end='')
        print(results.acc_balance)
    elif arg == 4:
         results = session.query(Deposits).filter(Deposits.user_id
           == user_details.user_id).all()
         print("Your Deposits History is as follows")
         for i in results:
             print("{} {} ".format(i.dep_id, i.user_id), end="")
             print("{} {} ".format(i.dep_date, i.amt_deposited), end="")
             print("{}".format(i.acc_balance))
    elif arg == 5:
         results = session.query(Withdrawals).filter(Accounts.user_id
           == user_details.user_id).all()
         print("Your Withdrawal History is as follows")
         for i in results:
             print("{} {} ".format(i.withd_id, i.user_id), end="")
             print("{} {} ".format(i.withd_date, i.amt_withdrawn), end="")
             print("{}".format(i.acc_balance))
